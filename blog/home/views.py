from django.shortcuts import render

posts = [
    {
        'title': 'Lord of the Rings',
        'description': 'The Lord of the Rings is an epic fantasy tale about a quest to destroy a powerful ring and defeat the Dark Lord Sauron. Its a story of courage, friendship, and the battle between good and evil.',
        'author': 'J.R.R Tolkein' 
    },
    {
        'title': 'Harry Potter',
        'description': "Harry Potter is a magical series about a young wizard, Harry, who attends Hogwarts School of Witchcraft and Wizardry. He battles the dark wizard Voldemort with his friends Ron and Hermione. It's a tale of friendship, courage, and the fight between good and evil.",
        'author': 'J.K. Rowling' 
    },
    {
        'title': 'The hunger Games',
        'description': "The Hunger Games is a dystopian trilogy where teens from twelve districts are forced to fight to the death in a televised event. Katniss Everdeen volunteers to save her sister, sparking a rebellion against the oppressive Capitol. It's a story about survival, sacrifice, and resistance.",
        'author': 'Suzanne Collins',

    },
    {
        'title': 'The Chronicles of Narnia',
        'description': "The Chronicles of Narnia is a series of fantasy novels by C.S. Lewis where children discover the magical land of Narnia. They encounter talking animals, mythical creatures, and the lion Aslan, battling against evil forces. It's a story of adventure, magic, and the struggle between good and evil.",
        'author': 'C.S Lewis',
    }
]



# Create your views here.
def home_view(request):
    context = {
        'titleSite' : 'Books & Coffe',
        'posts' : posts
    }
    return render(request, 'home/index.html', context)
