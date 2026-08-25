shelves = 8 
storage_bins = 5 


for shelf in range(shelves):
    print()
    for bin in range(storage_bins,):
        if (bin + 1) % 2 == 1:
            print(f"Shelf {shelf + 1} -  Bin {bin + 1}: FAIL ")
        else:
             print(f"Shelf {shelf + 1} -  Bin {bin + 1}: PASS")
        
        
        
