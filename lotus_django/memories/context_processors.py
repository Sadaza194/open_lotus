

def mobile(request):
    return {'is_mobile': request.user_agent.is_mobile}