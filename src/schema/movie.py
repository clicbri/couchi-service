from ariadne import gql

movie = gql("""
    type Movie {
        id: ID!
        title: String!
        year: String!
        synopsis: String!
        duration: Int
        genres: String
        created_at: String
        updated_at: String
    }
""")
