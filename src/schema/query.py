from ariadne import gql

query = gql("""
    type Query {
        hello: String
        movies: [Movie]!
    }
""")
