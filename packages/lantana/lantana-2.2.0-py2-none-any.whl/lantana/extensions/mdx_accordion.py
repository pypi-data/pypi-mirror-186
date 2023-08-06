import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def fence_accordion(source, language, css_class, options, md, 
            classes=None, id_value='', custom=False, **kwargs):
    
    if id_value=='':
        id_value = randomname(10)

    html = '<div class="accordion-item"><h2 class="accordion-header" id="{0}"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#{0}" aria-expanded="true" aria-controls="{0}">{1}</button></h2> <div id="{0}" class="accordion-collapse collapse show"><div class="accordion-body">{2}</div></div></div>'.format(id_value,css_class,source)
    
    print("--- accordion ---\n", html, "\n------")
    return html