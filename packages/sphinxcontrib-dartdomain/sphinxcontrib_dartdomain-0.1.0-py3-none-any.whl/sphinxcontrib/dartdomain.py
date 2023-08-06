"""The Dart domain."""

from __future__ import annotations

from typing import Any, Iterator, Tuple, cast

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType
from sphinx.domains.python import _pseudo_parse_arglist
from sphinx.environment import BuildEnvironment
from sphinx.locale import _, __
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx.util.docutils import SphinxDirective, switch_source_input
from sphinx.util.nodes import make_id, make_refnode, nested_parse_with_titles
from sphinx.util.typing import OptionSpec

logger = logging.getLogger(__name__)


class DartObject(ObjectDescription[Tuple[str, str]]):
    """
    Description of a Dart object.
    """
    #: If set to ``True`` this object is callable and a `desc_parameterlist` is
    #: added
    has_arguments = False

    #: If ``allow_nesting`` is ``True``, the object prefixes will be accumulated
    #: based on directive nesting
    allow_nesting = False

    option_spec: OptionSpec = {
        'noindex': directives.flag,
        'noindexentry': directives.flag,
        'nocontentsentry': directives.flag,
    }

    def get_display_prefix(self) -> list[Node]:
        #: what is displayed right before the documentation entry
        return []

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        """Breaks down construct signatures

        Parses out prefix and argument list from construct definition. The
        namespace and class will be determined by the nesting of domain
        directives.
        """
        sig = sig.strip()
        if '(' in sig and sig[-1:] == ')':
            member, arglist = sig.split('(', 1)
            member = member.strip()
            arglist = arglist[:-1].strip()
        else:
            member = sig
            arglist = None
        # If construct is nested, prefix the current prefix
        prefix = self.env.ref_context.get('dart:object', None)
        pkg_name = self.env.ref_context.get('dart:package')

        name = member
        try:
            member_prefix, member_name = member.rsplit('.', 1)
        except ValueError:
            member_name = name
            member_prefix = ''
        finally:
            name = member_name
            if prefix and member_prefix:
                prefix = '.'.join([prefix, member_prefix])
            elif prefix is None and member_prefix:
                prefix = member_prefix
        fullname = name
        if prefix:
            fullname = '.'.join([prefix, name])

        signode['package'] = pkg_name
        signode['object'] = prefix
        signode['fullname'] = fullname

        display_prefix = self.get_display_prefix()
        if display_prefix:
            signode += addnodes.desc_annotation('', '', *display_prefix)

        actual_prefix = None
        if prefix:
            actual_prefix = prefix
        elif pkg_name:
            actual_prefix = pkg_name
        if actual_prefix:
            addName = addnodes.desc_addname('', '')
            for p in actual_prefix.split('.'):
                addName += addnodes.desc_sig_name(p, p)
                addName += addnodes.desc_sig_punctuation('.', '.')
            signode += addName
        signode += addnodes.desc_name('', '', addnodes.desc_sig_name(name, name))
        if self.has_arguments:
            if not arglist:
                signode += addnodes.desc_parameterlist()
            else:
                _pseudo_parse_arglist(signode, arglist)
        return fullname, prefix

    def _object_hierarchy_parts(self, sig_node: desc_signature) -> tuple[str, ...]:
        if 'fullname' not in sig_node:
            return ()
        pkgname = sig_node.get('package')
        fullname = sig_node['fullname']

        if pkgname:
            return (pkgname, *fullname.split('.'))
        else:
            return tuple(fullname.split('.'))

    def add_target_and_index(self, name_obj: tuple[str, str], sig: str,
                             signode: desc_signature) -> None:
        pkg_name = self.env.ref_context.get('dart:package')
        fullname = (pkg_name + '.' if pkg_name else '') + name_obj[0]
        node_id = make_id(self.env, self.state.document, '', fullname)
        signode['ids'].append(node_id)
        self.state.document.note_explicit_target(signode)

        domain = cast(DartDomain, self.env.get_domain('dart'))
        domain.note_object(fullname, self.objtype, node_id, location=signode)

        if 'noindexentry' not in self.options:
            indextext = self.get_index_text(pkg_name, name_obj)
            if indextext:
                self.indexnode['entries'].append(('single', indextext, node_id, '', None))

    def get_index_text(self, objectname: str, name_obj: tuple[str, str]) -> str:
        name, obj = name_obj
        if self.objtype == 'function':
            if not obj:
                return _('%s() (built-in function)') % name
            return _('%s() (%s method)') % (name, obj)
        elif self.objtype == 'class':
            return _('%s() (class)') % name
        elif self.objtype == 'data':
            return _('%s (global variable or constant)') % name
        elif self.objtype == 'attribute':
            return _('%s (%s attribute)') % (name, obj)
        return ''

    def before_content(self) -> None:
        """Handle object nesting before content

        :py:class:`DartObject` represents Dart language constructs. For
        constructs that are nestable, this method will build up a stack of the
        nesting hierarchy so that it can be later de-nested correctly, in
        :py:meth:`after_content`.

        For constructs that aren't nestable, the stack is bypassed, and instead
        only the most recent object is tracked. This object prefix name will be
        removed with :py:meth:`after_content`.

        The following keys are used in ``self.env.ref_context``:

            dart:objects
                Stores the object prefix history. With each nested element, we
                add the object prefix to this list. When we exit that object's
                nesting level, :py:meth:`after_content` is triggered and the
                prefix is removed from the end of the list.

            dart:object
                Current object prefix. This should generally reflect the last
                element in the prefix history
        """
        prefix = None
        if self.names:
            (obj_name, obj_name_prefix) = self.names.pop()
            prefix = obj_name_prefix.strip('.') if obj_name_prefix else None
            if self.allow_nesting:
                prefix = obj_name
        if prefix:
            self.env.ref_context['dart:object'] = prefix
            if self.allow_nesting:
                objects = self.env.ref_context.setdefault('dart:objects', [])
                objects.append(prefix)

    def after_content(self) -> None:
        """Handle object de-nesting after content

        If this class is a nestable object, removing the last nested class prefix
        ends further nesting in the object.

        If this class is not a nestable object, the list of classes should not
        be altered as we didn't affect the nesting levels in
        :py:meth:`before_content`.
        """
        objects = self.env.ref_context.setdefault('dart:objects', [])
        if self.allow_nesting:
            try:
                objects.pop()
            except IndexError:
                pass
        self.env.ref_context['dart:object'] = (objects[-1] if len(objects) > 0
                                              else None)

    def make_old_id(self, fullname: str) -> str:
        """Generate old styled node_id for Dart objects.

        .. note:: Old Styled node_id was used until Sphinx-3.0.
                  This will be removed in Sphinx-5.0.
        """
        return fullname.replace('$', '_S_')

    def _toc_entry_name(self, sig_node: desc_signature) -> str:
        if not sig_node.get('_toc_parts'):
            return ''

        config = self.env.app.config
        objtype = sig_node.parent.get('objtype')
        if config.add_function_parentheses and objtype in {'function', 'method'}:
            parens = '()'
        else:
            parens = ''
        *parents, name = sig_node['_toc_parts']
        if config.toc_object_entries_show_parents == 'domain':
            return sig_node.get('fullname', name) + parens
        if config.toc_object_entries_show_parents == 'hide':
            return name + parens
        if config.toc_object_entries_show_parents == 'all':
            return '.'.join(parents + [name + parens])
        return ''


class DartCallable(DartObject):
    """Description of a Dart function, method or constructor."""
    has_arguments = True

    doc_field_types = [
        TypedField('arguments', label=_('Arguments'),
                   names=('argument', 'arg', 'parameter', 'param'),
                   typerolename='func', typenames=('paramtype', 'type')),
        GroupedField('errors', label=_('Throws'), rolename='func',
                     names=('throws', ),
                     can_collapse=True),
        Field('returnvalue', label=_('Returns'), has_arg=False,
              names=('returns', 'return')),
        Field('returntype', label=_('Return type'), has_arg=False,
              names=('rtype',)),
    ]


class DartClass(DartObject):
    """Like a callable but with a different prefix."""

    allow_nesting = True

    def get_display_prefix(self) -> list[Node]:
        return [addnodes.desc_sig_keyword('class', 'class'),
                addnodes.desc_sig_space()]


class DartPackage(SphinxDirective):
    """
    Directive to mark description of a new Dart package.

    This directive specifies the package name that will be used by objects that
    follow this directive.

    Options
    -------

    noindex
        If the ``noindex`` option is specified, no linkable elements will be
        created, and the package won't be added to the global package index.
        This is useful for splitting up the package definition across multiple
        sections or files.

    :param pkg_name: Package name
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {
        'noindex': directives.flag,
        'nocontentsentry': directives.flag,
    }

    def run(self) -> list[Node]:
        pkg_name = self.arguments[0].strip()
        self.env.ref_context['dart:package'] = pkg_name
        noindex = 'noindex' in self.options

        content_node: Element = nodes.section()
        with switch_source_input(self.state, self.content):
            # necessary so that the child nodes get the right source/line set
            content_node.document = self.state.document
            nested_parse_with_titles(self.state, self.content, content_node)

        ret: list[Node] = []
        if not noindex:
            domain = cast(DartDomain, self.env.get_domain('dart'))

            node_id = make_id(self.env, self.state.document, 'package', pkg_name)
            domain.note_package(pkg_name, node_id)
            # Make a duplicate entry in 'objects' to facilitate searching for
            # the package in DartDomain.find_obj()
            domain.note_object(pkg_name, 'package', node_id,
                               location=(self.env.docname, self.lineno))

            target = nodes.target('', '', ids=[node_id], ismod=True)
            self.state.document.note_explicit_target(target)
            ret.append(target)
            indextext = _('%s (package)') % pkg_name
            inode = addnodes.index(entries=[('single', indextext, node_id, '', None)])
            ret.append(inode)
        ret.extend(content_node.children)
        return ret

    def make_old_id(self, pkgname: str) -> str:
        """Generate old styled node_id for Dart packages.

        .. note:: Old Styled node_id was used until Sphinx-3.0.
                  This will be removed in Sphinx-5.0.
        """
        return 'package-' + pkgname


class DartXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> tuple[str, str]:
        # basically what sphinx.domains.python.PyXRefRole does
        refnode['dart:object'] = env.ref_context.get('dart:object')
        refnode['dart:package'] = env.ref_context.get('dart:package')
        if not has_explicit_title:
            title = title.lstrip('.')
            target = target.lstrip('~')
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot + 1:]
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class DartDomain(Domain):
    """Dart language domain."""
    name = 'dart'
    label = 'Dart'
    # if you add a new object type make sure to edit DartObject.get_index_string
    object_types = {
        'function':  ObjType(_('function'),  'func'),
        'method':    ObjType(_('method'),    'meth'),
        'class':     ObjType(_('class'),     'class'),
        'data':      ObjType(_('data'),      'data'),
        'attribute': ObjType(_('attribute'), 'attr'),
        'package':   ObjType(_('package'),  'pkg'),
    }
    directives = {
        'function':  DartCallable,
        'method':    DartCallable,
        'class':     DartClass,
        'data':      DartObject,
        'attribute': DartObject,
        'package':   DartPackage,
    }
    roles = {
        'func':  DartXRefRole(fix_parens=True),
        'meth':  DartXRefRole(fix_parens=True),
        'class': DartXRefRole(),
        'data':  DartXRefRole(),
        'attr':  DartXRefRole(),
        'pkg':   DartXRefRole(),
    }
    initial_data: dict[str, dict[str, tuple[str, str]]] = {
        'objects': {},   # fullname -> docname, node_id, objtype
        'packages': {},  # pkgname  -> docname, node_id
    }

    @property
    def objects(self) -> dict[str, tuple[str, str, str]]:
        return self.data.setdefault('objects', {})  # fullname -> docname, node_id, objtype

    def note_object(self, fullname: str, objtype: str, node_id: str,
                    location: Any = None) -> None:
        if fullname in self.objects:
            docname = self.objects[fullname][0]
            logger.warning(__('duplicate %s description of %s, other %s in %s'),
                           objtype, fullname, objtype, docname, location=location)
        self.objects[fullname] = (self.env.docname, node_id, objtype)

    @property
    def packages(self) -> dict[str, tuple[str, str]]:
        return self.data.setdefault('packages', {})  # pkgname -> docname, node_id

    def note_package(self, pkgname: str, node_id: str) -> None:
        self.packages[pkgname] = (self.env.docname, node_id)

    def clear_doc(self, docname: str) -> None:
        for fullname, (pkg_docname, _node_id, _l) in list(self.objects.items()):
            if pkg_docname == docname:
                del self.objects[fullname]
        for pkgname, (pkg_docname, _node_id) in list(self.packages.items()):
            if pkg_docname == docname:
                del self.packages[pkgname]

    def merge_domaindata(self, docnames: list[str], otherdata: dict[str, Any]) -> None:
        # XXX check duplicates
        for fullname, (fn, node_id, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.objects[fullname] = (fn, node_id, objtype)
        for pkg_name, (pkg_docname, node_id) in otherdata['packages'].items():
            if pkg_docname in docnames:
                self.packages[pkg_name] = (pkg_docname, node_id)

    def find_obj(
        self,
        env: BuildEnvironment,
        pkg_name: str,
        prefix: str,
        name: str,
        typ: str | None,
        searchorder: int = 0
    ) -> tuple[str | None, tuple[str, str, str] | None]:
        if name[-2:] == '()':
            name = name[:-2]

        searches = []
        if pkg_name and prefix:
            searches.append('.'.join([pkg_name, prefix, name]))
        if pkg_name:
            searches.append('.'.join([pkg_name, name]))
        if prefix:
            searches.append('.'.join([prefix, name]))
        searches.append(name)

        if searchorder == 0:
            searches.reverse()

        newname = None
        for search_name in searches:
            if search_name in self.objects:
                newname = search_name

        return newname, self.objects.get(newname)

    def resolve_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                     typ: str, target: str, node: pending_xref, contnode: Element
                     ) -> Element | None:
        pkg_name = node.get('dart:package')
        prefix = node.get('dart:object')
        searchorder = 1 if node.hasattr('refspecific') else 0
        name, obj = self.find_obj(env, pkg_name, prefix, target, typ, searchorder)
        if not obj:
            return None
        return make_refnode(builder, fromdocname, obj[0], obj[1], contnode, name)

    def resolve_any_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                         target: str, node: pending_xref, contnode: Element
                         ) -> list[tuple[str, Element]]:
        pkg_name = node.get('dart:package')
        prefix = node.get('dart:object')
        name, obj = self.find_obj(env, pkg_name, prefix, target, None, 1)
        if not obj:
            return []
        return [('dart:' + self.role_for_objtype(obj[2]),
                 make_refnode(builder, fromdocname, obj[0], obj[1], contnode, name))]

    def get_objects(self) -> Iterator[tuple[str, str, str, str, str, int]]:
        for refname, (docname, node_id, typ) in list(self.objects.items()):
            yield refname, refname, typ, docname, node_id, 1

    def get_full_qualified_name(self, node: Element) -> str | None:
        pkgname = node.get('dart:package')
        prefix = node.get('dart:object')
        target = node.get('reftarget')
        if target is None:
            return None
        else:
            return '.'.join(filter(None, [pkgname, prefix, target]))


def setup(app: Sphinx):
    app.add_domain(DartDomain)
