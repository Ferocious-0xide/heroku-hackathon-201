# scripts/dyno_manager.py
#!/usr/bin/env python3
"""
Dyno Management Script

This script helps manage different Heroku dyno configurations for various environments.
It provides commands to:
1. Scale dynos up/down
2. Change dyno types
3. Set up recommended configurations for different traffic levels
4. Estimate costs
"""

import os
import argparse
import json
from typing import Dict, List

# Dyno pricing (as of 2024)
DYNO_PRICES = {
    "basic": 5,
    "standard-1x": 25,
    "standard-2x": 50,
    "performance-m": 250,
    "performance-l": 500
}

# Pre-defined configurations for different scales
SCALE_CONFIGS = {
    "minimal": {
        "web": {"type": "basic", "quantity": 1},
        "worker": {"type": "basic", "quantity": 1}
    },
    "starter": {
        "web": {"type": "standard-1x", "quantity": 2},
        "worker": {"type": "standard-1x", "quantity": 1}
    },
    "business": {
        "web": {"type": "standard-2x", "quantity": 4},
        "worker": {"type": "standard-2x", "quantity": 2}
    },
    "enterprise": {
        "web": {"type": "performance-m", "quantity": 6},
        "worker": {"type": "performance-m", "quantity": 3}
    }
}

def calculate_monthly_cost(config: Dict) -> float:
    """Calculate the monthly cost for a given dyno configuration."""
    total_cost = 0
    for dyno_type, specs in config.items():
        dyno_price = DYNO_PRICES[specs["type"]]
        total_cost += dyno_price * specs["quantity"]
    return total_cost

def apply_configuration(app_name: str, config: Dict) -> None:
    """Apply a dyno configuration to a Heroku app using the Heroku CLI."""
    for dyno_type, specs in config.items():
        os.system(f'heroku ps:scale {dyno_type}={specs["quantity"]} --app {app_name}')
        os.system(f'heroku ps:type {dyno_type}={specs["type"]} --app {app_name}')

def validate_configuration(config: Dict) -> List[str]:
    """Validate a dyno configuration for common issues."""
    issues = []
    
    # Check for minimum web dynos
    web_dynos = config.get("web", {}).get("quantity", 0)
    if web_dynos < 1:
        issues.append("At least one web dyno is required")
    
    # Check for performance dyno limitations
    for dyno_type, specs in config.items():
        if specs["type"].startswith("performance"):
            if specs["quantity"] > 1 and dyno_type != "web":
                issues.append(f"Multiple performance dynos only supported for web processes")
    
    return issues

def main():
    parser = argparse.ArgumentParser(description="Manage Heroku dyno configurations")
    parser.add_argument("app_name", help="Heroku app name")
    parser.add_argument("--scale", choices=SCALE_CONFIGS.keys(), help="Apply a predefined scale configuration")
    parser.add_argument("--estimate", action="store_true", help="Estimate monthly cost")
    
    args = parser.parse_args()
    
    if args.scale:
        config = SCALE_CONFIGS[args.scale]
        issues = validate_configuration(config)
        
        if issues:
            print("Configuration issues found:")
            for issue in issues:
                print(f"- {issue}")
            return
        
        if args.estimate:
            cost = calculate_monthly_cost(config)
            print(f"Estimated monthly cost: ${cost}")
        else:
            print(f"Applying {args.scale} configuration to {args.app_name}...")
            apply_configuration(args.app_name, config)

if __name__ == "__main__":
    main()