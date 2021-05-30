from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from textblob import TextBlob 
import json
from scipy import spatial
import logging
LOGGER = logging.getLogger(__name__)

movie_correlation_matrix = {"Action":[1,0,1,1,1,0,0,1],
           "Romance":[1,1,0,1,0,1,0,0],
           "Horror":[1,1,1,1,1,0,0,0],
           "Mystry":[0,0,0,1,1,0,0,0],
           "Sci-Fi":[1,0,0,1,1,0,0,0],
           "Thriller":[1,0,1,1,0,0,0,0],
           "Adventure":[0,0,1,1,0,0,1,0],
           "Musical":[0,1,0,0,0,1,0,0],
           "Comedy":[0,0,0,0,0,1,1,1],
           "Cartoon":[0,0,0,0,0,0,1,1],
           "Fantasy":[1,0,0,1,1,0,0,0]
           }

@csrf_exempt
def input_data(request):
        LOGGER.info('Movie Prediction Method - Starts')

        quetion_list=[]
        for i in range(1,9):
           quetion_list.append(request.POST.get('ques' + str(i)))
        
        # Finding the movie genre using Cosine Similarity
        movie={}
        for key, value in movie_correlation_matrix.items():
            result = 1 - spatial.distance.cosine(quetion_list,value)
            movie[key]=result
        movie_genre=max(movie, key=movie.get)
        
        # Find the Sentiment type for the comment given for the movie
        comment=request.POST.get('comment')
        c=TextBlob(comment)
        val=c.sentiment[0]
        LOGGER.info('The sentiment score for the given comment is{}'.format(val))
        
        if(val>0.5):
            review="A Positive review for the "+movie_genre+" movie" 
        elif(val==0.5):
            review="A Neutral review for the "+movie_genre+" movie"
        else:
            review="A Negative review for the "+movie_genre+" movie"
            
        LOGGER.info('The review of the movie is {}'.format(review))
        LOGGER.info('Movie Prediction Method - Ends')
        return HttpResponse(json.dumps({ 'review' : review}), content_type='application/json')
    
    
