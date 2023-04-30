from models import db
from models import UserModel, PathogenModel, SequenceModel
from resources import users, pathogens, sequences

user_model_list = [UserModel(user[0],
                             user[1],
                             user[2],
                             user[3],
                             user[4],
                             user[5],
                             user[6]) for user in users]

print(user_model_list)

for user_model in user_model_list:
    user_model.save_to_db()

pathogen_model_list = [PathogenModel(pathogen[0],
                                     pathogen[1],
                                     pathogen[2],
                                     pathogen[3],
                                     pathogen[4],
                                     pathogen[5]
                                     ) for pathogen in pathogens]

for pathogen_model in pathogen_model_list:
    pathogen_model.save_to_db()

sequence_model_list = [SequenceModel(sequence[0],
                                     sequence[1]) for sequence in sequences]

for sequence_model in sequence_model_list:
    sequence_model.save_to_db()


