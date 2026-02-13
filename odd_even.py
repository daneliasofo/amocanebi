#გაქვთ მოცემული ინტების ლისტი nums, დაარეთურნეთ რამდენი ლუწი რიცხვია ამ ლისტში. მაგალითად: 
#Input: nums = [12,345,2,6,7896]
#Output: 2

def even(nums):
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
    return even

print(even([12, 345, 2, 6, 7896]))  


#გაქვთ მოცემული ინტების ლისტი nums, ლისტში ყველა 0 უნდა გადაიტანოთ ლისტის ბოლოს ხოლო დანარჩენი რიცხვები უნდა დალაგოთ იგივე თანმიმდევრობით ლისტის დასაწყისში. მაგალითად:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]


def zeros(nums):
    result = []
    zero_count = 0
    
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)
    
    result += [0] * zero_count
    return result


nums = [0,1,0,3,12]
print(zeros(nums))


#გაქვთ მოცემული ინტების ლისტი nums, ლისტში ყველა კენტი რიცხვი უნდა გადაიტანოთ ლისტის ბოლოს ხოლო ყველა ლუწი რიცხვები უნდა გადაიტანოთ ლისტის დასაწყისში. მაგალითად:
#Input: nums = [3,1,2,4]
#Output: [2,4,3,1] ან [4,2,3,1] ან [2,4,1,3] ან [4,2,1,3]

def int_list(nums):
    evens = []
    odds = []
    
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    return evens + odds


nums = [3,1,2,4]
print(int_list(nums))



