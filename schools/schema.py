
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from .models import Hall as HallModel, Lesson as LessonModel, User as UserModel


class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
        
class HallSchema(SQLAlchemyObjectType):
    class Meta:
        model = HallModel
        interfaces = (relay.Node,)
        
class LessonSchema(SQLAlchemyObjectType):
    class Meta:
        model = LessonModel
        interfaces = (relay.Node,)
        
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    all_users = SQLAlchemyConnectionField(UserSchema.connection)
    
    all_halls = SQLAlchemyConnectionField(HallSchema.connection)
    
    all_lessons = SQLAlchemyConnectionField(LessonSchema.connection)
       

    
schema = graphene.Schema(query=Query)