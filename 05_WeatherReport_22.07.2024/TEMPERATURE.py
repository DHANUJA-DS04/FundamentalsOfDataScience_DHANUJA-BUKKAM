def readcsv(file_path):
    formatted_data = []
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    for line in lines[1:]:  # Skip header
        if line.strip():
            date_str, temp_str, wind_str = line.split(',')
            day, month, year = date_str.split('/')
            formatted_date = f"{day}/{month}/{year}"
            try:
                temperature = float(temp_str)
                wind_speed = int(wind_str)
                formatted_data.append((formatted_date, temperature, wind_speed))
            except ValueError:
                print(f"Warning: Skipping malformed line: {line}")
    
    return formatted_data

def avgofmonth(data, month):
    total_temp = 0
    count = 0
    for date, temp, windspeed in data:
        if date.split('/')[1] == month:
            total_temp += temp
            count += 1
    return total_temp / count if count > 0 else None

def avgtempbetmonth(data, start_month, end_month):
    total_temp = 0
    count = 0
    
    for date_str, temperature, _ in data:
        _, month, _ = date_str.split('/')
        if start_month <= month <= end_month:
            total_temp += temperature
            count += 1
    
    return total_temp / count if count > 0 else None

def lowestspeed(data, start_month, end_month):
    min_temp = float('inf')
    wind_speed = None
    
    for date_str, temperature, w_speed in data:
        _, month, _ = date_str.split('/')
        if start_month <= month <= end_month:
            if temperature < min_temp:
                min_temp = temperature
                wind_speed = w_speed
    
    return wind_speed if wind_speed is not None else None

def main():
    file_path = file_path = "C:\\Users\\amogh\\Desktop\\fundamentalsofds\\fundamentalsofds\\Q5\\temp.csv"

    data = readcsv(file_path)

    print(f"Average temperature for March: {avgofmonth(data, '03'):.2f}")

    avg_temp = avgtempbetmonth(data, '09', '11')
    print(f"Average Temperature from September to November: {avg_temp:.2f}")

    wind_speed = lowestspeed(data, '09', '11')
    print(f"Wind Speed when Temperature is Lowest from September to November: {wind_speed}")

if __name__ == "__main__":
    main()
