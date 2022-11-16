Створити веб-застосунок з graphql api:
1. Містить наступні таблиці в БД
Hall 
* id
* city: str
* street: str
User
* id: int
* name: str
Lesson
* id
* hall -> Hall
* coach -> User
2. Містить graphql api з наступною схемою:
type Hall {
    id: Int!
    city: String
    street: String
}
type User {
    id: Int!
    name: String
}
type Lesson {
    id: Int!
    hall: Hall
    coach: User
}
type Query {
    getAllLessons: [Lesson!]!  // Повинна витягуват всі уроки з бази
}
3.
* Мова Python
* Бекенд бібліотека aiohttp
* Для графу бібліотека може бути будь-яка, але використання graphene буде плюсом
* База даних postgresql
* Взаємодія з базою через sqlalchemy (в асинхронному режимі)
* API має бути робочим (тобто Query.getAllLessons має повертати усі уроки з потрібними полями)
Запит яким буду тестувати:
{
    getAllLessons {
        id
        hall {
            id
            city
            street
        }
        coach {
            id
            name
        }
    }
}
