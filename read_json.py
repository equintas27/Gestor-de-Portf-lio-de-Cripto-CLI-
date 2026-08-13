import json
from typing import Dict, Any, Optional

def read_json(path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = json.load(f)
            return content
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return None
    except json.JSONDecodeError:
        print ("Json Inválido")
        return None