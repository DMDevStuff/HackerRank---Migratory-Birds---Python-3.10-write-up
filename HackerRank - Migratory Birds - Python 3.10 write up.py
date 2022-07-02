##    https://www.hackerrank.com/challenges/migratory-birds/problem
##
##    Given an array of bird sightings where every element represents a bird
##    type id, determine the id of the most frequently sighted type. If more
##    than 1 type has been spotted that maximum amount, return the smallest of
##    their ids.

##### ##### ##### #####

# changed input from arr to bird_sighting_list

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of bird_sighting_list
#   Algo:
#       pass through the given list and keep track of the bird ids
#       and the number of times they occur with a dictionary
#       key:value = bird_id:number_of_occurrences
#       pass through the occurrence table and keep track of the most occurrences
#       and the smallest associated id
#       return id

def migratoryBirds(bird_sighting_list):

    bird_occurrence_table = dict()

    for bird_id in bird_sighting_list:

        try:
            bird_occurrence_table[bird_id] += 1

        except:
            bird_occurrence_table[bird_id] = 1

    min_bird_id = None
    max_number_of_sightings = 0

    for bird_id in bird_occurrence_table:

        if bird_occurrence_table[bird_id] > max_number_of_sightings:

            max_number_of_sightings = bird_occurrence_table[bird_id]
            min_bird_id = bird_id

        elif bird_occurrence_table[bird_id] == max_number_of_sightings:

            min_bird_id = min(min_bird_id, bird_id)

    return min_bird_id
