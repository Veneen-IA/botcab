import os
from supabase import create_client
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

def get_supabase_client():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        raise ValueError("Les variables d'environnement SUPABASE_URL et SUPABASE_KEY doivent être définies")
    
    return create_client(supabase_url, supabase_key)
