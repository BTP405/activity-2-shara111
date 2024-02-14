import matplotlib.pyplot as plt

def graphSnowFall(t): 
    with open(t, 'r') as f:
        ranges = f.readlines()
        cleaned_ranges = []  # List to hold cleaned and converted integer values

        for each in ranges:
            try:
                # Attempt to convert each line to int, stripping newline characters
                num = int(each.strip())
                cleaned_ranges.append(num)
            except ValueError:
                # Skip lines that cannot be converted to int
                continue
            
        # Initialize counters
        range_0_10 = range_11_20 = range_21_30 = range_31_40 = range_41_50 = 0

        for i in cleaned_ranges:
            if i <= 10: 
                range_0_10 += 1
            elif 11 <= i <= 20:  
                range_11_20 += 1
            elif 21 <= i <= 30:  
                range_21_30 += 1
            elif 31 <= i <= 40:  
                range_31_40 += 1
            else: 
                range_41_50 += 1

        x = ['0 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50']
        y = [range_0_10, range_11_20, range_21_30, range_31_40, range_41_50]
        plt.bar(x, y)
        plt.title('Snowfall')
        plt.xlabel('Range (cm)')
        plt.ylabel('Amount')
        plt.yticks([0, 1, 2, 3, 4, 5])
        plt.show()

graphSnowFall('q2.txt')
