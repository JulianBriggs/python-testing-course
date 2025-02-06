import random

def randomly_sample_and_filter_participants(
    participants: list, 
    sample_size: int, 
    min_age: int, 
    max_age: int, 
    min_height: int, 
    max_height: int
):
    """Participants is a list of tuples, containing the age and height of each participant
    participants = [
                      {age: 25, height: 180}, 
                      {age: 30, height: 170}, 
                      {age: 35, height: 160}, 
    ]
    """
    
    # Get the indexes to sample
    indexes = random.sample(range(len(participants)), sample_size)

    # Get the sampled participants
    sampled_participants = []
    for i in indexes:
        sampled_participants.append(participants[i])
    
    # Remove participants that are outside the age range
    sampled_participants_age_filtered = []
    for participant in sampled_participants:
        if participant['age'] >= min_age and participant['age'] <= max_age:
            sampled_participants_age_filtered.append(participant)
    
    # Remove participants that are outside the height range
    sampled_participants_height_filtered = []
    for participant in sampled_participants_age_filtered:
        if participant['height'] >= min_height and participant['height'] <= max_height:
            sampled_participants_height_filtered.append(participant)

    return sampled_participants_height_filtered

import random

def randomly_sample_and_filter_participants2(
    participants: list, 
    sample_size: int, 
    min_age: int, 
    max_age: int, 
    min_height: int, 
    max_height: int
):
    """Participants is a list of tuples, containing the age and height of each participant
    participants = [
                      {age: 25, height: 180}, 
                      {age: 30, height: 170}, 
                      {age: 35, height: 160}, 
    ]
    """
    
    #~ # Get the indexes to sample
    #~ indexes = random.sample(range(len(participants)), sample_size)
    

    # Get the sampled participants
    #~ sampled_participants = []
    #~ for i in indexes:
        #~ sampled_participants.append(participants[i])
    sampled_participants=get_sampled_participants([],participants)
    
    # Remove participants that are outside the age range
    sampled_participants_age_filtered = []
    for participant in sampled_participants:
        if participant['age'] >= min_age and participant['age'] <= max_age:
            sampled_participants_age_filtered.append(participant)
    
    # Remove participants that are outside the height range
    sampled_participants_height_filtered = []
    for participant in sampled_participants_age_filtered:
        if participant['height'] >= min_height and participant['height'] <= max_height:
            sampled_participants_height_filtered.append(participant)

    return sampled_participants_height_filtered
    
def get_indexes(participants,sample_size):
    # Get the indexes to sample
    return random.sample(range(len(participants)), sample_size)
    
    
	
def get_sampled_participants(sampled_participants,participants):
	for i in indexes:
		sampled_participants.append(participants[i])
