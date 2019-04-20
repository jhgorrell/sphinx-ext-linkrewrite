#
# ht-sphinx/sphinx-ext-linkrewrite/sphinx_ext_linkrewrite/__init__.py ---
#


"""sphinx_ext_linkrewrite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rewrites the ``refuri`` of :py:class:`nodes.reference` from
a list of rewrite rules.

The rules can be put into ``conf.py``, or put into the document.

The rules are matched in the order they occur in the
document, then from the list ``linkrewrite_rules`` from
``conf.py``.

Rules in the document:
::

    .. linkrewrite::
       :from: SOURCE_REGEX
       :to:   DEST_PATTERN

Or in ``conf.py``:
::

     linkrewrite_rules = [
         [from_regex, to_pattern],
     ]

Only the first matching rule is applied.
"""

#####

import re

import docutils.parsers.rst.directives
from docutils import (
    nodes,
)

import sphinx
from sphinx.transforms import (
    SphinxTransform,
)
from sphinx.util.docutils import (
    SphinxDirective,
)

#####


def rewrite_link(link, rules):
    """
    Attempt to rewrite the link using the list of rules.

    :param link:   Url string.
    :param rules:  A list of [ from, to ] pairs.

    Returns the rewritten link or None.
    """
    if not link:
        return None
    if not rules:
        return None

    for rule_from, rule_to in rules:
        m = re.match(rule_from, link)
        if m:
            return m.expand(rule_to)

    return None

#####


class LinkRewriteRuleNode(nodes.Element):
    """A spot to park a rewrite rule after the directive is read.

    A LinkRewriteDirective creates them, then
    LinkRewriteTransform gathers them to make the list of
    rules.
    """

    def __init__(self,
                 *args,
                 rule_from=None,
                 rule_to=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.rule_from = rule_from
        self.rule_to = rule_to

    def __repr__(self):
        return "#<{} from={!r} to={!r}>".format(
            self.__class__.__name__,
            self.rule_from,
            self.rule_to)


class LinkRewriteDirective(SphinxDirective):
    """
    The parser for the ``linkrewrite`` directive.
    """

    final_argument_whitespace = False
    has_content = False
    optional_arguments = 0
    required_arguments = 0

    option_spec = {
        'from': docutils.parsers.rst.directives.unchanged_required,
        'to': docutils.parsers.rst.directives.unchanged_required,
    }

    def run(self):
        """Turn the directive into a node.

        This is done so the rules can be found by
        :py:class:`LinkRewriteTransform` later.
        """
        if False:
            print("{}: self.options={}".format(
                self.__class__.__name__,
                self.options))

        node = LinkRewriteRuleNode(
            rule_from=self.options["from"],
            rule_to=self.options["to"])

        return [node]


class LinkRewriteTransform(SphinxTransform):
    """Transform the node.reference refuris with the list of rewrite rules.
    """

    default_priority = 299

    def apply(self, **kwargs):
        """Apply the transform to rewrite the refuris of the references.
        """

        # Assemble our rules.
        rules = []

        # Find the document-local rules.
        for node in self.document.traverse(LinkRewriteRuleNode):
            # Add them...
            rules.append([node.rule_from, node.rule_to])
            # ...and snip them out.
            node.parent.remove(node)

        # Now, add the rules from the config file.
        rules.extend(getattr(self.config, "linkrewrite_rules", []))

        # Ready to rewrite all the reference nodes.
        for node in self.document.traverse(nodes.reference):
            refuri = node.attributes["refuri"]
            node.attributes["refuri"] = rewrite_link(refuri, rules) or refuri

        return True


def setup(app):
    """
    Register this extention with the Sphinx app.
    """
    # type: (Sphinx) -> Dict[str, Any]
    app.add_node(LinkRewriteRuleNode)
    app.add_config_value('linkrewrite_rules', [], 'html')
    app.add_directive('linkrewrite', LinkRewriteDirective)
    app.add_transform(LinkRewriteTransform)

    return {
        'version': sphinx.__display_version__,
        'env_version': 1,
        'parallel_read_safe': True
    }
