from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from prediction import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from prediction.models import Estimation

import pickle
import pandas as pd


# Chargement du modèle sauvegardé avec pickle
with open('prediction/model.pickle2', 'rb') as f:
    model = pickle.load(f)


def accueil(request):
    return render(request, 'accueil.html')

def estimation(request):
    form = forms.EstimationForm()
    predicted_price = None
    if request.method == 'POST':
        form = forms.EstimationForm(request.POST)
        if form.is_valid():
            m2_living = form.cleaned_data['m2_living']
            grade = form.cleaned_data['grade']
            view = form.cleaned_data['view']
            m2_above = form.cleaned_data['m2_above']
            bathrooms = form.cleaned_data['bathrooms']
            zipcode = form.cleaned_data['zipcode']
            m2_basement = form.cleaned_data['m2_basement']
            bedrooms = form.cleaned_data['bedrooms']
            waterfront = form.cleaned_data['waterfront']
            floors = form.cleaned_data['floors']
            yr_renovated = form.cleaned_data['yr_renovated']
            m2_lot = form.cleaned_data['m2_lot']
            yr_built = form.cleaned_data['yr_built']
            condition = form.cleaned_data['condition']
            
            X = pd.DataFrame({'bedrooms': [bedrooms],
                              'bathrooms': [bathrooms],
                              'm2_living': [m2_living],
                              'm2_lot': [m2_lot],
                              'floors': [floors],
                              'waterfront': [waterfront],
                              'view': [view],
                              'condition': [condition],
                              'grade': [grade],
                              'm2_above': [m2_above],
                              'yr_built': [yr_built],
                              'm2_basement': [m2_basement],
                              'yr_renovated': [yr_renovated],
                              'zipcode': [zipcode]
                              })
            predicted_price = round(model.predict(X)[0])
            estimation = form.save()
            estimation.predicted_price = round(predicted_price)
            estimation.user = request.user
            estimation.save()
            return redirect('estimation-details',estimation.id)
    else : 
        form = forms.EstimationForm()
    return render(request,'estimation.html', {'form':form, 'predicted_price':predicted_price})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'login.html', context={'form': form, 'message': message})
    
    
@login_required(login_url='login')
def logout_user(request):
    """
    Vue pour la déconnexion de l'utilisateur connecté. Déconnecte l'utilisateur actuel et le redirige vers la
    page d'accueil.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec une redirection vers la page d'accueil
    """
    logout(request)
    return redirect('accueil')

def signup(request):
    """
    Vue pour la page d'inscription du site. Affiche un formulaire d'inscription permettant à un nouvel utilisateur
    de créer un compte. Si le formulaire est soumis et valide, le nouvel utilisateur est enregistré et connecté automatiquement, puis redirigé vers la
    page d'accueil.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec un template rendu contenant un formulaire d'inscription
      - si le formulaire est soumis et valide, un nouvel utilisateur est créé et connecté, puis l'utilisateur est
        redirigé vers la page d'accueil
      - sinon, le formulaire est réaffiché avec les erreurs de validation appropriées
    """
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    return render(request, 'signup.html', {'form':form})


@login_required(login_url='login')
def user_detail(request):
    """
    Vue affichant les détails de l'utilisateur connecté ainsi qu'un bouton pour modifier son compte.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec un template rendu contenant les détails de l'utilisateur connecté et les actions possibles
    """
    return render(request, 'mon-compte.html')


@login_required(login_url='login')
def modifier_compte(request):
    """
    Fonction de vue qui permet à un utilisateur connecté de modifier les informations de son compte.

    Si la méthode HTTP de la requête est 'POST', les données du formulaire sont validées et enregistrées,
    et l'utilisateur est redirigé vers l'URL 'mon-compte'. Si la méthode n'est pas 'POST', le formulaire est
    initialisé avec les données de l'utilisateur actuel et affiché sur le modèle 'modifier-mon-compte'.

    Args:
        request: L'objet de requête HTTP envoyé par le client.

    Returns:
        Un objet de réponse HTTP qui contient le modèle 'modifier-mon-compte' rendu avec l'objet de formulaire
        comme données de contexte.
    """
    user = request.user
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, instance = user)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mon-compte')

    else : 
        form = forms.SignUpForm(instance = user)
    return render(request, 'modifier-compte.html', {'form':form})


@login_required(login_url='login')
def liste_estimations(request):
    """
    Fonction de vue qui affiche une liste de rendez-vous.

    La fonction récupère tous les rendez-vous à partir de la base de données, puis les
    envoie au modèle 'mes-rdv.html' pour les afficher.

    Args:
        request: L'objet de requête HTTP envoyé par le client.

    Returns:
        Un objet de réponse HTTP qui contient le modèle 'mes-rdv.html' rendu avec la liste de rendez-vous en tant que
        données de contexte.
    """
    liste_estimations = Estimation.objects.filter(user=request.user)
    return render(request, 'mes-estimations.html', {'liste_estimations':liste_estimations})


@login_required(login_url='login')
def estimation_details(request, id):
    estimation = Estimation.objects.get(id=id)
    return render(request, 'estimation-details.html', {'estimation':estimation})


@login_required(login_url='login')
def modifier_estimation(request,id):
    estimation = Estimation.objects.get(id=id)
    form = forms.EstimationForm(request.POST, instance = estimation)
    predicted_price = None
    if request.method == 'POST':
        form = forms.EstimationForm(request.POST, instance = estimation)
        if form.is_valid():
            m2_living = form.cleaned_data['m2_living']
            grade = form.cleaned_data['grade']
            view = form.cleaned_data['view']
            m2_above = form.cleaned_data['m2_above']
            bathrooms = form.cleaned_data['bathrooms']
            zipcode = form.cleaned_data['zipcode']
            m2_basement = form.cleaned_data['m2_basement']
            bedrooms = form.cleaned_data['bedrooms']
            waterfront = form.cleaned_data['waterfront']
            floors = form.cleaned_data['floors']
            yr_renovated = form.cleaned_data['yr_renovated']
            m2_lot = form.cleaned_data['m2_lot']
            yr_built = form.cleaned_data['yr_built']
            condition = form.cleaned_data['condition']
            
            X = pd.DataFrame({'bedrooms': [bedrooms],
                              'bathrooms': [bathrooms],
                              'm2_living': [m2_living],
                              'm2_lot': [m2_lot],
                              'floors': [floors],
                              'waterfront': [waterfront],
                              'view': [view],
                              'condition': [condition],
                              'grade': [grade],
                              'm2_above': [m2_above],
                              'yr_built': [yr_built],
                              'm2_basement': [m2_basement],
                              'yr_renovated': [yr_renovated],
                              'zipcode': [zipcode]
                              })
            predicted_price = round(model.predict(X)[0])
            estimation = form.save()
            estimation.predicted_price = predicted_price
            estimation.user = request.user
            estimation.save()
            return redirect('estimation-details',estimation.id)

    else : 
        form = forms.EstimationForm(instance = estimation)
    return render(request, 'modifier-estimation.html', {'form':form})