import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Hall as HallModel, Lesson as LessonModel, User as UserModel

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
     
        
class HallSchema(SQLAlchemyObjectType):
    class Meta:
        model = HallModel
  
        
class LessonSchema(SQLAlchemyObjectType):
    class Meta:
        model = LessonModel
     
        
class Query(graphene.ObjectType):

    getAllUsers = graphene.List(UserSchema)
    getAllHalls = graphene.List(HallSchema)
    getAllLessons = graphene.List(LessonSchema)

    async def resolve_getAllUsers(self, info):
        query = UserSchema.get_query(info) 
        return query.all()
    
    async def resolve_getAllHalls(root,info):
        query = HallSchema.get_query(info) 
        return query.all()

    async def resolve_getAllLessons(root,info):
        query = LessonSchema.get_query(info) 
        return query.all()
    
schema = graphene.Schema(query=Query)
