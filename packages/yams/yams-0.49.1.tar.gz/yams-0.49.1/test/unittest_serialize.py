from logilab.common import testlib

from yams.buildobjs import register_base_types, EntityType, RelationType, RelationDefinition
from yams import schema, serialize


class MyTests(testlib.TestCase):
    def test_yams_serialize(self):
        s = schema.Schema("Unknown")
        register_base_types(s)
        e2 = EntityType("Ent2")
        s.add_entity_type(e2)
        e1 = EntityType("Ent1")
        e1.specialized_type = "Ent2"
        s.add_entity_type(e1)
        s.add_relation_type(RelationType("attr1"))
        s.add_relation_def(RelationDefinition("Ent1", "attr1", "String"))
        out = serialize.serialize_to_python(s)
        self.assertMultiLineEqual(
            out,
            "\n".join(
                [
                    "from yams.buildobjs import *",
                    "",
                    "class Ent2(EntityType):",
                    "    pass",
                    "",
                    "class Ent1(Ent2):",
                    "    attr1 = String()",
                    "\n",
                ]
            ),
        )

    def test_yams_serialize_multiple_inheritance(self):
        # declaration order is important, we want to test ordered_nodes()
        # so add entity Ent1 before Base0 and Base1
        s = schema.Schema("Unknown")
        register_base_types(s)
        e1 = EntityType("Ent1")
        e1.specialized_type = "Base0, Base1"
        s.add_entity_type(e1)
        b0 = EntityType("Base0")
        s.add_entity_type(b0)
        b1 = EntityType("Base1")
        s.add_entity_type(b1)
        s.add_relation_type(RelationType("attr1"))
        s.add_relation_def(RelationDefinition("Ent1", "attr1", "String"))
        out = serialize.serialize_to_python(s)
        self.assertMultiLineEqual(
            out,
            "\n".join(
                [
                    "from yams.buildobjs import *",
                    "",
                    "class Base1(EntityType):",
                    "    pass",
                    "",
                    "class Base0(EntityType):",
                    "    pass",
                    "",
                    "class Ent1(Base0, Base1):",
                    "    attr1 = String()",
                    "\n",
                ]
            ),
        )


if __name__ == "__main__":
    testlib.unittest_main()
