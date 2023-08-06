

# def test_fetched_fields_visitor_gets_scalar_fields():
#     ast = parse("""
#         query {
#             LabelsMany(where: {name: {_eq: "Parlophone"}}) {
#                 name
#                 establishedYear
#                 artists {
#                     name
#                     albums(where: { title: { _eq: "Help!" } }) {
#                         title
#                     }
#                 }
#             }
#         }
#     """)
#     visitor = FetchedFieldsVisitor()
#     result = visit(ast, visitor)
#     assert visitor.fields_by_key is None
