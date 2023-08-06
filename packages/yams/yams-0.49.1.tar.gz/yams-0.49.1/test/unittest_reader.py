# copyright 2004-2014 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of yams.
#
# yams is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# yams is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with yams. If not, see <http://www.gnu.org/licenses/>.
"""unit tests for module yams.reader"""

import sys
import os.path as osp
from datetime import datetime, date, time

from logilab.common.testlib import TestCase, unittest_main

from yams import BadSchemaDefinition, DEFAULT_RELPERMS, DEFAULT_ATTRPERMS
from yams.schema import Schema
from yams.reader import SchemaLoader, build_schema_from_namespace
from yams.constraints import StaticVocabularyConstraint, SizeConstraint
from yams.buildobjs import (
    EntityType,
    RelationType,
    RelationDefinition,
    SubjectRelation,
    ComputedRelation,
    Int,
    String,
    Float,
    Datetime,
    Date,
    Boolean,
)

sys.path.insert(0, osp.dirname(__file__))


class SchemaLoaderTC(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = SchemaLoader().load([cls.datadir])

    # test helper functions ###################################################

    def test_get_schema_files(self):
        files = [osp.basename(f) for f in SchemaLoader().get_schema_files(self.datadir)]
        self.assertEqual(files[0], "__init__.py")
        self.assertEqual(
            sorted(files), ["Company.py", "Dates.py", "State.py", "__init__.py", "schema.py"]
        )

    # test load_schema read entity and relation types #######################

    def test_load_schema(self):
        self.assertIsInstance(self.schema, Schema)
        self.assertEqual(self.schema.name, "NoName")
        self.assertListEqual(
            sorted(self.schema.entities()),
            [
                "Affaire",
                "BigInt",
                "Boolean",
                "Bytes",
                "Company",
                "Date",
                "Datetest",
                "Datetime",
                "Decimal",
                "Division",
                "EPermission",
                "Eetype",
                "Employee",
                "Float",
                "Int",
                "Interval",
                "Note",
                "Password",
                "Person",
                "Salaried",
                "Societe",
                "State",
                "String",
                "Subcompany",
                "Subdivision",
                "TZDatetime",
                "TZTime",
                "Time",
                "pkginfo",
            ],
        )
        self.assertListEqual(
            sorted(self.schema.relations()),
            [
                "ad1",
                "ad2",
                "ad3",
                "adel",
                "ass",
                "author",
                "author_email",
                "concerne",
                "copyright",
                "cp",
                "d1",
                "d2",
                "date",
                "datenaiss",
                "debian_handler",
                "description",
                "division_of",
                "dt1",
                "dt2",
                "eid",
                "evaluee",
                "fax",
                "final",
                "initial_state",
                "inline_rel",
                "license",
                "long_desc",
                "mailinglist",
                "meta",
                "modname",
                "name",
                "next_state",
                "nom",
                "obj_wildcard",
                "para",
                "prenom",
                "promo",
                "ref",
                "require_permission",
                "rncs",
                "salary",
                "sexe",
                "short_desc",
                "state_of",
                "subcompany_of",
                "subdivision_of",
                "subj_wildcard",
                "sujet",
                "sym_rel",
                "t1",
                "t2",
                "tel",
                "test",
                "titre",
                "travaille",
                "type",
                "version",
                "ville",
                "web",
                "works_for",
            ],
        )

    def test_entity_schema_for(self):
        entity_schema = self.schema.entity_schema_for("Societe")
        self.assertEqual(entity_schema.description, "")
        self.assertEqual(entity_schema.final, False)
        self.assertListEqual(
            sorted(list(entity_schema.subject_relations.values())),
            [
                "ad1",
                "ad2",
                "ad3",
                "cp",
                "evaluee",
                "fax",
                "nom",
                "rncs",
                "subj_wildcard",
                "tel",
                "ville",
                "web",
            ],
        )
        self.assertListEqual(
            sorted(list(entity_schema.object_relations.values())),
            ["concerne", "obj_wildcard", "travaille"],
        )

        entity_schema = self.schema.entity_schema_for("Eetype")
        self.assertEqual(
            entity_schema.description, "define an entity type, used to build the application schema"
        )
        self.assertEqual(entity_schema.final, False)
        self.assertListEqual(
            sorted(str(r) for r in entity_schema.subject_relations.values()),
            ["description", "final", "initial_state", "meta", "name", "subj_wildcard"],
        )
        self.assertListEqual(
            sorted(str(r) for r in entity_schema.object_relations.values()),
            ["obj_wildcard", "state_of"],
        )

        entity_schema = self.schema.entity_schema_for("Boolean")
        self.assertEqual(entity_schema.description, "")
        self.assertEqual(entity_schema.final, True)
        self.assertListEqual(sorted(list(entity_schema.subject_relations.values())), [])
        self.assertListEqual(
            sorted(list(entity_schema.object_relations.values())), ["final", "meta", "test"]
        )

    # test base entity type's subject relation properties #####################

    def test_indexed(self):
        entity_schema = self.schema.entity_schema_for("Person")
        self.assertFalse(entity_schema.relation_definition("nom").indexed)
        entity_schema = self.schema.entity_schema_for("State")
        self.assertTrue(entity_schema.relation_definition("name").indexed)

    def test_uid(self):
        entity_schema = self.schema.entity_schema_for("State")
        self.assertTrue(entity_schema.relation_definition("eid").uid)
        self.assertFalse(entity_schema.relation_definition("name").uid)

    def test_fulltextindexed(self):
        entity_schema = self.schema.entity_schema_for("Person")
        self.assertRaises(
            AttributeError, getattr, entity_schema.relation_definition("tel"), "fulltextindexed"
        )  # tel is an INT
        self.assertTrue(entity_schema.relation_definition("nom").fulltextindexed)
        self.assertTrue(entity_schema.relation_definition("prenom").fulltextindexed)
        self.assertFalse(entity_schema.relation_definition("sexe").fulltextindexed)
        indexable = sorted(entity_schema.indexable_attributes())
        self.assertEqual(["nom", "prenom", "titre"], indexable)
        self.assertEqual(self.schema.relation_schema_for("works_for").fulltext_container, None)
        self.assertEqual(
            self.schema.relation_schema_for("require_permission").fulltext_container, "subject"
        )
        entity_schema = self.schema.entity_schema_for("Company")
        indexable = sorted(entity_schema.indexable_attributes())
        self.assertEqual([], indexable)
        indexable = sorted(entity_schema.fulltext_relations())
        self.assertEqual([("require_permission", "subject")], indexable)
        containers = sorted(entity_schema.fulltext_containers())
        self.assertEqual([], containers)
        entity_schema = self.schema.entity_schema_for("EPermission")
        indexable = sorted(entity_schema.indexable_attributes())
        self.assertEqual(["name"], indexable)
        indexable = sorted(entity_schema.fulltext_relations())
        self.assertEqual([], indexable)
        containers = sorted(entity_schema.fulltext_containers())
        self.assertEqual([("require_permission", "subject")], containers)

    def test_internationalizable(self):
        entity_schema = self.schema.entity_schema_for("Eetype")
        self.assertTrue(entity_schema.relation_definition("name").internationalizable)
        entity_schema = self.schema.entity_schema_for("State")
        self.assertTrue(entity_schema.relation_definition("name").internationalizable)
        entity_schema = self.schema.entity_schema_for("Societe")
        self.assertFalse(entity_schema.relation_definition("ad1").internationalizable)

    # test advanced entity type's subject relation properties #################

    def test_vocabulary(self):
        entity_schema = self.schema.entity_schema_for("pkginfo")
        self.assertEqual(entity_schema.vocabulary("license"), ("GPL", "ZPL"))
        self.assertEqual(entity_schema.vocabulary("debian_handler"), ("machin", "bidule"))

    def test_default(self):
        entity_schema = self.schema.entity_schema_for("pkginfo")
        self.assertEqual(entity_schema.default("version"), "0.1")
        self.assertEqual(entity_schema.default("license"), None)

    # test relation type properties ###########################################

    def test_relation_schema_for(self):
        relation_schema = self.schema.relation_schema_for("evaluee")
        self.assertEqual(relation_schema.symmetric, False)
        self.assertEqual(relation_schema.description, "")
        self.assertEqual(relation_schema.final, False)
        self.assertListEqual(sorted(relation_schema.subjects()), ["Person", "Salaried", "Societe"])
        self.assertListEqual(sorted(relation_schema.objects()), ["Note"])

        relation_schema = self.schema.relation_schema_for("sym_rel")
        self.assertEqual(relation_schema.symmetric, True)
        self.assertEqual(relation_schema.description, "")
        self.assertEqual(relation_schema.final, False)
        self.assertListEqual(sorted(relation_schema.subjects()), ["Affaire", "Person", "Salaried"])
        self.assertListEqual(sorted(relation_schema.objects()), ["Affaire", "Person", "Salaried"])

        relation_schema = self.schema.relation_schema_for("initial_state")
        self.assertEqual(relation_schema.symmetric, False)
        self.assertEqual(
            relation_schema.description,
            "indicate which state should be used by default when an entity using states is created",
        )
        self.assertEqual(relation_schema.final, False)
        self.assertListEqual(sorted(relation_schema.subjects()), ["Eetype"])
        self.assertListEqual(sorted(relation_schema.objects()), ["State"])

        relation_schema = self.schema.relation_schema_for("name")
        self.assertEqual(relation_schema.symmetric, False)
        self.assertEqual(relation_schema.description, "")
        self.assertEqual(relation_schema.final, True)
        self.assertListEqual(
            sorted(relation_schema.subjects()),
            ["Company", "Division", "EPermission", "Eetype", "State", "Subcompany", "Subdivision"],
        )
        self.assertListEqual(sorted(relation_schema.objects()), ["String"])

    def test_cardinality(self):
        relation_schema = self.schema.relation_schema_for("evaluee")
        self.assertEqual(relation_schema.relation_definition("Person", "Note").cardinality, "**")
        relation_schema = self.schema.relation_schema_for("inline_rel")
        self.assertEqual(relation_schema.relation_definition("Affaire", "Person").cardinality, "?*")
        relation_schema = self.schema.relation_schema_for("initial_state")
        self.assertEqual(relation_schema.relation_definition("Eetype", "State").cardinality, "?*")
        relation_schema = self.schema.relation_schema_for("state_of")
        self.assertEqual(relation_schema.relation_definition("State", "Eetype").cardinality, "+*")
        relation_schema = self.schema.relation_schema_for("name")
        self.assertEqual(relation_schema.relation_definition("State", "String").cardinality, "11")
        relation_schema = self.schema.relation_schema_for("description")
        self.assertEqual(relation_schema.relation_definition("State", "String").cardinality, "?1")

    def test_constraints(self):
        entity_schema = self.schema.entity_schema_for("Person")
        self.assertEqual(len(entity_schema.relation_definition("nom").constraints), 1)
        self.assertEqual(len(entity_schema.relation_definition("promo").constraints), 2)
        self.assertEqual(len(entity_schema.relation_definition("tel").constraints), 0)
        entity_schema = self.schema.entity_schema_for("State")
        self.assertEqual(len(entity_schema.relation_definition("name").constraints), 1)
        self.assertEqual(len(entity_schema.relation_definition("description").constraints), 0)
        entity_schema = self.schema.entity_schema_for("Eetype")
        self.assertEqual(len(entity_schema.relation_definition("name").constraints), 2)

    def test_inlined(self):
        relation_schema = self.schema.relation_schema_for("evaluee")
        self.assertEqual(relation_schema.inlined, False)
        relation_schema = self.schema.relation_schema_for("state_of")
        self.assertEqual(relation_schema.inlined, False)
        relation_schema = self.schema.relation_schema_for("inline_rel")
        self.assertEqual(relation_schema.inlined, True)
        relation_schema = self.schema.relation_schema_for("initial_state")
        self.assertEqual(relation_schema.inlined, True)

    def test_relation_permissions(self):
        relation_schema = self.schema.relation_schema_for("evaluee")
        self.assertEqual(
            relation_schema.relation_definition("Person", "Note").permissions,
            {"read": ("managers",), "delete": ("managers",), "add": ("managers",)},
        )
        self.assertEqual(
            relation_schema.relation_definition("Societe", "Note").permissions,
            {"read": ("managers",), "delete": ("managers",), "add": ("managers",)},
        )
        relation_schema = self.schema.relation_schema_for("concerne")
        self.assertEqual(
            relation_schema.relation_definition("Person", "Affaire").permissions,
            {"read": ("managers",), "delete": ("managers",), "add": ("managers",)},
        )
        self.assertEqual(
            relation_schema.relation_definition("Affaire", "Societe").permissions, DEFAULT_RELPERMS
        )
        relation_schema = self.schema.relation_schema_for("travaille")
        self.assertEqual(
            relation_schema.relation_definition("Person", "Societe").permissions,
            {"read": (), "add": (), "delete": ("managers",)},
        )

    def test_attributes_permissions(self):
        relation_schema = self.schema.relation_schema_for("name")
        self.assertEqual(
            relation_schema.relation_definition("Company", "String").permissions, DEFAULT_ATTRPERMS
        )
        relation_schema = self.schema.relation_schema_for("tel")
        self.assertEqual(
            relation_schema.relation_definition("Person", "Int").permissions,
            {"read": (), "add": ("managers",), "update": ("managers",)},
        )

    def test_entity_permissions(self):
        entity_schema = self.schema.entity_schema_for("State")
        self.assertEqual(
            entity_schema.permissions,
            {
                "read": (
                    "managers",
                    "users",
                    "guests",
                ),
                "add": (
                    "managers",
                    "users",
                ),
                "delete": (
                    "managers",
                    "owners",
                ),
                "update": (
                    "managers",
                    "owners",
                ),
            },
        )

        entity_schema = self.schema.entity_schema_for("Eetype")
        self.assertEqual(
            entity_schema.permissions,
            {
                "read": (
                    "managers",
                    "users",
                    "guests",
                ),
                "add": ("managers",),
                "delete": ("managers",),
                "update": (
                    "managers",
                    "owners",
                ),
            },
        )

        entity_schema = self.schema.entity_schema_for("Person")
        self.assertEqual(
            entity_schema.permissions,
            {
                "read": (
                    "managers",
                    "users",
                    "guests",
                ),
                "add": (
                    "managers",
                    "users",
                ),
                "delete": (
                    "managers",
                    "owners",
                ),
                "update": (
                    "managers",
                    "owners",
                ),
            },
        )


# def test_nonregr_using_tuple_as_relation_target(self):
#          relation_schema = schema.relation_schema_for('see_also')
#          self.assertEqual(relation_schema.symmetric, False)
#          self.assertEqual(relation_schema.description, '')
#          self.assertEqual(relation_schema.final, False)
#          self.assertListEqual(sorted(relation_schema.subjects()), ['Employee'])
#          self.assertListEqual(sorted(relation_schema.objects()), ['Company', 'Division'])
#


class SchemaLoaderModnamesTC(SchemaLoaderTC):
    @classmethod
    def setUpClass(cls):
        def modnames():
            yield ("data", "data.schema")
            for name in ["State", "Dates", "Company", "schema"]:
                yield ("data", ".".join(["data", "schema", name]))

        cls.schema = SchemaLoader().load(modnames())


class BasePerson(EntityType):
    firstname = String(vocabulary=("logilab", "caesium"), maxsize=10)
    lastname = String(constraints=[StaticVocabularyConstraint(["logilab", "caesium"])])


class Person(BasePerson):
    email = String()


class Employee(Person):
    company = String(vocabulary=("logilab", "caesium"))


class Student(Person):
    __specializes_schema__ = True
    college = String()


class X(Student):
    pass


class Foo(EntityType):
    i = Int(required=True, metadata={"name": String()})
    f = Float()
    d = Datetime()


class PySchemaTC(TestCase):
    def test_python_inheritance(self):
        bp = BasePerson()
        p = Person()
        e = Employee()
        self.assertEqual([r.name for r in bp.__relations__], ["firstname", "lastname"])
        self.assertEqual([r.name for r in p.__relations__], ["firstname", "lastname", "email"])
        self.assertEqual(
            [r.name for r in e.__relations__], ["firstname", "lastname", "email", "company"]
        )

    def test_schema_extension(self):
        s = Student()
        self.assertEqual(
            [r.name for r in s.__relations__], ["firstname", "lastname", "email", "college"]
        )
        self.assertEqual(s.specialized_type, "Person")
        x = X()
        self.assertEqual(x.specialized_type, None)

    def test_relationtype(self):
        foo = Foo()
        self.assertEqual(
            ["Int", "String", "Float", "Datetime"], [r.entity_type for r in foo.__relations__]
        )
        self.assertEqual(foo.__relations__[0].cardinality, "11")
        self.assertEqual(foo.__relations__[2].cardinality, "?1")

    def test_maxsize(self):
        bp = BasePerson()

        def maxsize(e):
            for e in e.constraints:
                if isinstance(e, SizeConstraint):
                    return e.max

        self.assertEqual(maxsize(bp.__relations__[0]), 7)
        # self.assertEqual(maxsize(bp.__relations__[1]), 7)
        emp = Employee()
        self.assertEqual(maxsize(emp.__relations__[3]), 7)

    def test_metadata(self):
        foo = Foo()
        self.assertEqual("i_name", foo.__relations__[1].name)

    def test_date_defaults(self):
        _today = date.today()
        _now = datetime.now()
        schema = SchemaLoader().load([self.datadir])
        datetest = schema.entity_schema_for("Datetest")
        dt1 = datetest.default("dt1")
        dt2 = datetest.default("dt2")
        d1 = datetest.default("d1")
        d2 = datetest.default("d2")
        t1 = datetest.default("t1")
        t2 = datetest.default("t2")
        # datetimes
        self.assertIsInstance(dt1, datetime)
        # there's no easy way to test NOW (except monkey patching now() itself)
        delta = dt1 - _now
        self.assertTrue(abs(delta.seconds) < 5)
        self.assertEqual(date(dt2.year, dt2.month, dt2.day), _today)
        self.assertIsInstance(dt2, datetime)
        # dates
        self.assertEqual(d1, _today)
        self.assertIsInstance(d1, date)
        self.assertEqual(d2, date(2007, 12, 11))
        self.assertIsInstance(d2, date)
        # times
        self.assertEqual(t1, time(8, 40))
        self.assertIsInstance(t1, time)
        self.assertEqual(t2, time(9, 45))
        self.assertIsInstance(t2, time)


class SchemaLoaderTC2(TestCase):
    def tearDown(self):
        SchemaLoader.main_schema_directory = "schema"

    def assertBadInlinedMessage(self, error):
        try:
            self.assertEqual(
                "conflicting values False/True for property inlined of relation 'rel'", str(error)
            )
        except AssertionError:
            self.assertEqual(
                "conflicting values True/False for property inlined of relation 'rel'", str(error)
            )

    def test_bad_relation_type_inlined_conflict1(self):
        class Anentity(EntityType):
            rel = SubjectRelation("Anentity", inlined=True)

        class Anotherentity(EntityType):
            rel = SubjectRelation("Anentity", inlined=False)

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(locals().items())
        self.assertBadInlinedMessage(cm.exception)

    def test_bad_relation_type_inlined_conflict2(self):
        class Anentity(EntityType):
            rel = SubjectRelation("Anentity", inlined=True)

        class rel(RelationType):
            inlined = False

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(locals().items())
        self.assertBadInlinedMessage(cm.exception)

    def test_bad_int_size_constraint(self):
        class Entity(EntityType):
            attr = Int(maxsize=40)

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(locals().items())
        self.assertEqual("size constraint doesn't apply to Int entity type", str(cm.exception))

    def test_bad_vocab_and_size(self):
        class Entity(EntityType):
            attr = String(
                constraints=[StaticVocabularyConstraint(["ab", "abc"]), SizeConstraint(2)]
            )
            # "auto-fixed" when using:
            # vocabulary=['ab', 'abc'], maxsize=1)

        with self.assertRaises(BadSchemaDefinition) as cm:
            schema = build_schema_from_namespace(locals().items())
        self.assertEqual(
            "size constraint set to 2 but vocabulary contains string of greater size",
            str(cm.exception),
        )

    def test_bad_relation_type_relation_definition_conflict(self):
        class foo(RelationType):
            __permissions__ = {"read": ()}

        class Entity(EntityType):
            foo = String(__permissions__={"add": ()})

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(locals().items())
        self.assertEqual(
            (
                "conflicting values {'add': ()}/{'read': ()} "
                "for property __permissions__ of relation 'foo'"
            ),
            str(cm.exception),
        )

    def test_schema(self):
        class Anentity(EntityType):
            rel = SubjectRelation("Anentity", inlined=True)

        class Anotherentity(EntityType):
            rel = SubjectRelation("Anentity")

        class rel(RelationType):
            composite = "subject"
            cardinality = "1*"
            symmetric = True

        schema = build_schema_from_namespace(locals().items())
        self.assertEqual("<builtin>", schema["Anentity"].package)
        relation = schema["rel"]
        self.assertEqual(True, rel.symmetric)
        self.assertEqual(True, rel.inlined)
        self.assertEqual("<builtin>", rel.package)
        relation_definition1 = relation.relation_definition("Anentity", "Anentity")
        self.assertEqual("subject", relation_definition1.composite)
        self.assertEqual("1*", relation_definition1.cardinality)
        self.assertEqual("<builtin>", relation_definition1.package)
        relation_definition2 = relation.relation_definition("Anotherentity", "Anentity")
        self.assertEqual("subject", relation_definition2.composite)
        self.assertEqual("1*", relation_definition2.cardinality)
        self.assertEqual("<builtin>", relation_definition2.package)

    def test_imports(self):
        schema = SchemaLoader().load([self.datadir, self.datadir + "2"], "Test")
        self.assertEqual(
            {"read": (), "add": (), "update": (), "delete": ()}, schema["Affaire"].permissions
        )
        self.assertEqual(
            [str(r) for r, at in schema["MyNote"].attribute_definitions()],
            ["date", "type", "para", "text"],
        )

    def test_duplicated_relation_type(self):
        loader = SchemaLoader()
        loader.defined = {}

        class RT1(RelationType):
            pass

        loader.add_definition(RT1)
        with self.assertRaises(BadSchemaDefinition) as cm:
            loader.add_definition(RT1)
        self.assertEqual(str(cm.exception), "duplicated relation type for RT1")

    def test_relation_type_priority(self):
        loader = SchemaLoader()
        loader.defined = {}

        class RT1Def(RelationDefinition):
            name = "RT1"
            subject = "Whatever"
            object = "Whatever"

        class RT1(RelationType):
            pass

        loader.add_definition(RT1Def)
        loader.add_definition(RT1)
        self.assertEqual(loader.defined["RT1"], RT1)

    def test_unfinalized_manipulation(self):
        class MyEntity(EntityType):
            base_arg_b = String()
            base_arg_a = Boolean()
            base_sub = SubjectRelation("MyOtherEntity")

        class base_obj(RelationDefinition):
            subject = "MyOtherEntity"
            object = "MyEntity"

        class MyOtherEntity(EntityType):
            base_o_obj = SubjectRelation("MyEntity")

        class base_o_sub(RelationDefinition):
            subject = "MyEntity"
            object = "MyOtherEntity"

        MyEntity.add_relation(Date(), name="new_arg_a")
        MyEntity.add_relation(Int(), name="new_arg_b")
        MyEntity.add_relation(SubjectRelation("MyOtherEntity"), name="new_sub")
        MyOtherEntity.add_relation(SubjectRelation("MyEntity"), name="new_o_obj")

        class new_obj(RelationDefinition):
            subject = "MyOtherEntity"
            object = "MyEntity"

        class new_o_sub(RelationDefinition):
            subject = "MyEntity"
            object = "MyOtherEntity"

        schema = build_schema_from_namespace(locals().items())
        self.assertIn("MyEntity", schema.entities())
        my_entity = schema["MyEntity"]
        attributes_def = my_entity.attribute_definitions()
        attributes = sorted(attr[0].type for attr in attributes_def)
        self.assertEqual(["base_arg_a", "base_arg_b", "new_arg_a", "new_arg_b"], attributes)
        relations_def = my_entity.relation_definitions()
        relations = sorted(rel[0].type for rel in relations_def)
        self.assertEqual(
            [
                "base_o_obj",
                "base_o_sub",
                "base_obj",
                "base_sub",
                "new_o_obj",
                "new_o_sub",
                "new_obj",
                "new_sub",
            ],
            relations,
        )

    def test_post_build_callback(self):
        SchemaLoader.main_schema_directory = "schema_post_build_callback"
        schema = SchemaLoader().load([self.datadir], "Test")
        self.assertIn("Toto", schema.entities())


class BuildSchemaTC(TestCase):
    def test_build_schema(self):
        class Question(EntityType):
            number = Int()
            text = String()

        class Form(EntityType):
            title = String()

        class in_form(RelationDefinition):
            subject = "Question"
            object = "Form"
            cardinality = "*1"

        schema = build_schema_from_namespace(vars().items())
        entities = [x for x in schema.entities() if not x.final]
        self.assertCountEqual(["Form", "Question"], entities)
        relations = [x for x in schema.relations() if not x.final]
        self.assertCountEqual(["in_form"], relations)


class ComputedSchemaTC(TestCase):
    def test_computed_schema(self):
        class Societe(EntityType):
            name = String()

        class Employe(EntityType):
            name = String()

        class travaille(RelationDefinition):
            subject = "Employe"
            object = "Societe"

        class est_paye_par(ComputedRelation):
            __permissions__ = {"read": ("managers", "users")}
            rule = "S travaille O"

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual("S travaille O", schema["est_paye_par"].rule)
        self.assertEqual({"read": ("managers", "users")}, schema["est_paye_par"].permissions)

    def test_no_relation_definition_from_computedrelation(self):
        class Personne(EntityType):
            name = String()

        class Mafieu(EntityType):
            nickname = String()

        class est_paye_par(ComputedRelation):
            rule = "S travaille O"

        class est_soudoye_par(RelationDefinition):
            name = "est_paye_par"
            subject = "Personne"
            object = "Mafieu"

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(vars().items())
        self.assertEqual(
            'Cannot add relation definition "est_paye_par" '
            "because an homonymous computed relation already "
            'exists with rule "S travaille O"',
            str(cm.exception),
        )

    def test_invalid_attributes_in_computedrelation(self):
        class Societe(EntityType):
            name = String()

        class Employe(EntityType):
            name = String()

        class travaille(RelationDefinition):
            subject = "Employe"
            object = "Societe"

        class est_paye_par(ComputedRelation):
            rule = "S travaille O"
            inlined = True

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(vars().items())
        self.assertEqual("Computed relation has no inlined attribute", str(cm.exception))

    def test_invalid_permissions_in_computedrelation(self):
        class Societe(EntityType):
            name = String()

        class Employe(EntityType):
            name = String()

        class travaille(RelationDefinition):
            subject = "Employe"
            object = "Societe"

        class est_paye_par(ComputedRelation):
            __permissions__ = {
                "read": ("managers", "users", "guests"),
                "add": ("hacker inside!",),
                "delete": (),
            }
            rule = "S travaille O"

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(vars().items())
        self.assertEqual(
            "Cannot set add/delete permissions on computed relation est_paye_par", str(cm.exception)
        )

    def test_computed_attribute_type(self):
        class Entity(EntityType):
            attr = Int(formula="Any Z WHERE X oattr Z")
            oattr = String()

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual(
            "Any Z WHERE X oattr Z", schema["Entity"].relation_definition("attr").formula
        )
        self.assertIsNone(schema["Entity"].relation_definition("oattr").formula)

    def test_computed_attribute_relation_definition(self):
        class Entity(EntityType):
            oattr = String()

        class attr(RelationDefinition):
            subject = "Entity"
            object = "Int"
            formula = "Any Z WHERE X oattr Z"

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual(
            "Any Z WHERE X oattr Z", schema["Entity"].relation_definition("attr").formula
        )
        self.assertIsNone(schema["Entity"].relation_definition("oattr").formula)

    def test_computed_attribute_perms(self):
        class Entity(EntityType):
            oattr = String()

        class attr(RelationDefinition):
            subject = "Entity"
            object = "Int"
            formula = "Any Z WHERE X oattr Z"

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual(
            {"read": ("managers", "users", "guests"), "update": (), "add": ()},
            schema["attr"].relation_definition("Entity", "Int").permissions,
        )

    def test_cannot_set_addupdate_perms_on_computed_attribute(self):
        class Entity(EntityType):
            oattr = String()

        class attr(RelationDefinition):
            __permissions__ = {
                "read": ("managers", "users", "guests"),
                "add": ("hacker inside!",),
                "update": (),
            }
            subject = "Entity"
            object = "Int"
            formula = "Any Z WHERE X oattr Z"

        with self.assertRaises(BadSchemaDefinition) as cm:
            build_schema_from_namespace(vars().items())
        self.assertEqual(
            "Cannot set add/update permissions on computed attribute Entity.attr[Int]",
            str(cm.exception),
        )

    def test_override_read_perms_on_computed_attribute(self):
        class Entity(EntityType):
            oattr = String()
            subjrel = SubjectRelation("String")

        class attr(RelationDefinition):
            __permissions__ = {"read": ("clows",), "add": (), "update": ()}
            subject = "Entity"
            object = "Int"
            formula = "Any Z WHERE X oattr Z"

        class foo(RelationDefinition):
            subject = "Entity"
            object = "Boolean"

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual(
            {"read": ("clows",), "update": (), "add": ()},
            schema["attr"].relation_definition("Entity", "Int").permissions,
        )
        self.assertEqual(
            DEFAULT_ATTRPERMS, schema["foo"].relation_definition("Entity", "Boolean").permissions
        )

    def test_computed_attribute_subjrel(self):
        class Entity(EntityType):
            oattr = String()
            attr = SubjectRelation("Int", formula="Any Z WHERE X oattr Z")

        schema = build_schema_from_namespace(vars().items())
        self.assertEqual(
            "Any Z WHERE X oattr Z", schema["attr"].relation_definition("Entity", "Int").formula
        )


if __name__ == "__main__":
    unittest_main()
