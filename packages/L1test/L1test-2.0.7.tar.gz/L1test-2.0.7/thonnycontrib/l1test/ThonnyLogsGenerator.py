'''
Permet de générer pour le plugin de log une synthèse des tests exécutés.
Corentin.
'''

from thonny import get_workbench

#Attention si le nom change ici, il faut aussi le changer dans Thonny-LoggingPlugin
NOM_EVENT_TEST = "l1Tests"
NOM_EVENT_DOC = "l1Tests.DocGenerator"
wb = get_workbench()

def log_in_thonny(test_results,selected):
    for i in test_results :
        for j in test_results[i] :
            wb.event_generate(NOM_EVENT_TEST,None,selected = selected, name = i.name, **vars(j))

def log_doc_in_thonny(node):
    wb.event_generate(NOM_EVENT_DOC,None, name = node.name)
#La fonction anonyme car il faut une fonction pour bind, avec un argument parce qu'elle reçoit l'événement.    
wb.bind(NOM_EVENT_TEST,lambda x : 0 ,True)
wb.bind(NOM_EVENT_DOC,lambda x : 0 ,True)
