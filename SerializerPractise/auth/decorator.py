

def IsAuthenticated_User(func):

    def authentication_check(request,*args,**kwargs):


        token=request.META.get('HTTP_AUTHORIZATION')
        # token=args[0]
        print(token,'---->authentication_check')


        return func(request,*args,**kwargs)
    return authentication_check

