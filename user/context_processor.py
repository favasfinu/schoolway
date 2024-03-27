# from account.models import likes

def hi(request):
    return{"hi":"hello"}

# def like_count(request):
#     count=likes.objects.filter(user=request.user).count()
#     print(count)
#     return {"count":count}