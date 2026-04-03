from supabase import create_client, Client

SUPABASE_URL = "https://hlxvzkmkplfbwwptuqdb.supabase.co"
SUPABASE_KEY = "sb_publishable_pkl95D1OZ2FHHsGD2zCLdg_9yKUVQ1R"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)