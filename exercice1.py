"""
TP2 – Exercice 1 : Analyse des modules de la station spatiale ORBIT-X

Objectif :
Analyser les modules de la station afin d'extraire des statistiques utiles
pour la planification de la maintenance.

Un module est représenté par :
    nom_module : (cout_maintenance, temps_intervention, criticite)

Exemple :
modules = {
    'Laboratoire': (120, 15, 8),
    'Habitat': (200, 10, 9),
    'Observatoire': (150, 20, 6)
}
"""

# -------------------------------------------------------------------
# 1) Analyse des modules
# -------------------------------------------------------------------


def analyser_modules(modules):
    """
    Analyse les modules de la station.

    Args:
        modules (dict): {nom_module: (cout, temps, criticite)}

    Returns:
        dict contenant :
            - 'module_plus_critique' : str ou None
            - 'cout_moyen' : float
            - 'temps_moyen' : float
    """

    stats = {
        'module_plus_critique': None,
        'cout_moyen': 0,
        'temps_moyen': 0
    }

    # TODO 1 : Gérer le cas où le dictionnaire est vide
    # Dans ce cas, retourner stats tel quel
    if not modules or len(modules) == 0:
        return stats    

    # TODO 2 : Parcourir les modules
    # - Identifier le module ayant le meilleur ratio criticite / temps_intervention
    #   ⚠️ Ignorer les modules avec temps_intervention == 0
    #   ⚠️ En cas d’égalité, conserver le premier module rencontré
    for nom_module, (_ , temps, criticite) in modules.items():
        if temps > 0:  
            ratio = criticite / temps
            if (stats['module_plus_critique'] is None or
                    ratio > modules[stats['module_plus_critique']][2] / modules[stats['module_plus_critique']][1]):
                stats['module_plus_critique'] = nom_module
    

    # TODO 3 : Calculer les moyennes
    # - cout_moyen = somme_couts / nombre_modules
    # - temps_moyen = somme_temps / nombre_modules
    cout_total = 0
    temps_total = 0
   
    cout_total = sum(cout for cout, _, _ in modules.values())
    temps_total = sum(temps for _, temps, _ in modules.values())
    nombre_modules = len(modules)
    if nombre_modules > 0:
        stats['cout_moyen'] = cout_total / nombre_modules
        stats['temps_moyen'] = temps_total / nombre_modules

    return stats

# -------------------------------------------------------------------
# 2) Regroupement des modules par type
# -------------------------------------------------------------------


def regrouper_modules_par_type(modules, types):
    """
    Regroupe les modules par type.

    Args:
        modules (dict): dictionnaire des modules
        types (dict): {nom_module: type}

    Returns:
        dict: {type: [liste des modules]}
    """

    modules_par_type = {}

    # TODO :
    # Pour chaque module :
    #   - Vérifier s’il existe dans le dictionnaire types
    #   - Ajouter le module dans la liste correspondant à son type
    #   - Créer la liste si elle n’existe pas encore
    # ⚠️ Ignorer silencieusement les modules sans type
    for nom_module in modules.keys():
        if nom_module in types:
            type_module = types[nom_module]
            if type_module in modules_par_type:
                modules_par_type[type_module].append(nom_module)
            else:
                modules_par_type[type_module] = [nom_module]
    return modules_par_type

# -------------------------------------------------------------------
# 3) Calcul du cout total
# -------------------------------------------------------------------


def calculer_cout_total(modules, interventions):
    """
    Calcule le coût total de maintenance prévu.

    Args:
        modules (dict): {nom_module: (cout, temps, criticite)}
        interventions (dict): {nom_module: nombre_interventions}

    Returns:
        float: coût total
    """
 
    # TODO :
    # Pour chaque module dans interventions :
    #   - Vérifier qu’il existe dans modules
    #   - Ajouter à cout_total le cout total de maintenance du module étant donné le nombre d'interventions
    # ⚠️ Ignorer les modules absents de modules
    for nom_module, nombre_interventions in interventions.items():
        if nom_module in modules:
            cout_module = modules[nom_module][0]  
            cout_total += cout_module * nombre_interventions
    return cout_total

# -------------------------------------------------------------------
# TESTS main
# -------------------------------------------------------------------


if __name__ == "__main__":
    modules_test = {
        'Laboratoire': (120, 15, 8),
        'Habitat': (200, 10, 9),
        'Observatoire': (150, 20, 6)
    }

    types_test = {
        'Laboratoire': 'science',
        'Habitat': 'vie',
        'Observatoire': 'science'
    }

    interventions_test = {
        'Laboratoire': 2,
        'Habitat': 1
    }

    print(analyser_modules(modules_test))
    print(regrouper_modules_par_type(modules_test, types_test))
    print(calculer_cout_total(modules_test, interventions_test))
