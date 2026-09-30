# 28 Eylül 2026 - Binary Search
# Coding Interview University yol haritası

def binary_search(dizi, hedef):
    """
    Sıralı dizide binary search yapar.
    Hedefin indeksini döndürür, bulunamazsa -1 döndürür.
    """
    left = 0
    right = len(dizi) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if dizi[mid] == hedef:
            return mid  # Bulundu!
        elif dizi[mid] < hedef:
            left = mid + 1  # Sağ yarıya git
        else:
            right = mid - 1  # Sol yarıya git
    
    return -1  # Bulunamadı


# Test
if __name__ == "__main__":
    dizi = [3, 5, 8, 9]
    
    # Test 1: Hedef 8
    hedef = 8
    sonuc = binary_search(dizi, hedef)
    print(f"Hedef {hedef}, indeks: {sonuc}")
    
    # Test 2: Hedef 3
    hedef = 3
    sonuc = binary_search(dizi, hedef)
    print(f"Hedef {hedef}, indeks: {sonuc}")
    
    # Test 3: Hedef 10 (dizide yok)
    hedef = 10
    sonuc = binary_search(dizi, hedef)
    print(f"Hedef {hedef}, indeks: {sonuc}")
