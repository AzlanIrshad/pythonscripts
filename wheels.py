def chooseFleets(wheels):
    results = []
    for total_wheels in wheels:
        count = 0
        # x represents the number of 4-wheeled vehicles
        for x in range(total_wheels // 4 + 1):
            remaining_wheels = total_wheels - 4 * x
            # y represents the number of 2-wheeled vehicles
            if remaining_wheels % 2 == 0:
                count += 1
        results.append(count)
    return results

wheels = [6, 5,8]
print(chooseFleets(wheels))