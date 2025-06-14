# -*- coding: utf-8 -*-
"""Control Flow and Quality Control Simulation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qyjLyRaC-OTmlqGcS3h-uJtIeQWwPqoI
"""

import random

# Function to check product quality
def is_product_acceptable(length, weight, smoothness):
    """
    Returns True if product passes all quality checks, else False.
    """
    return (5.0 <= length <= 7.5) and (15 <= weight <= 25) and (smoothness > 7.5)

# Generate a batch of products (for demo purposes)
def generate_batch(batch_size):
    """
    Generates a list of random product measurements.
    Each product is a dictionary with length, weight, and smoothness.
    """
    batch = []
    for _ in range(batch_size):
        product = {
            "length": round(random.uniform(4.0, 9.0), 2),       # cm
            "weight": round(random.uniform(10, 30), 1),         # g
            "smoothness": round(random.uniform(5.0, 10.0), 2)   # rating out of 10
        }
        batch.append(product)
    return batch

# Main simulation
def run_quality_control(batch_size):
    print(f"\n🚀 Running Quality Control on Batch of {batch_size} Products\n")

    batch = generate_batch(batch_size)

    # DEBUG: Confirm the batch has items
    print(f"DEBUG: Batch generated with {len(batch)} products.")

    passed = []
    failed = []
    defective_count = 0

    for idx, product in enumerate(batch, start=1):
        length = product["length"]
        weight = product["weight"]
        smoothness = product["smoothness"]

        if is_product_acceptable(length, weight, smoothness):
            status = "✅ PASSED"
            passed.append(product)
        else:
            status = "❌ FAILED"
            failed.append(product)
            defective_count += 1

        print(f"Product {idx}: Length={length} cm, Weight={weight} g, Smoothness={smoothness} → {status}")

def run_quality_control(batch_size):
    # For demo purposes, define dummy passed and failed lists
    passed = [1, 2, 3]
    failed = [4, 5]

    print("\n📊 Summary")
    print("Total Products Checked:", batch_size)
    print("Products Passed:", len(passed))
    print("Products Failed:", len(failed))

# Call the function outside its definition
run_quality_control(10)