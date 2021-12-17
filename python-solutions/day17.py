def parse_target_area(target: str):
    target = target.replace("target area: ", "")
    x_str, y_str = target.split(", ")
    x_str = x_str.replace("x=", "")
    y_str = y_str.replace("y=", "")

    x_start, x_end = x_str.split("..")
    y_start, y_end = y_str.split("..")

    return {
        "x": range(int(x_start), int(x_end) + 1),
        "y": range(int(y_start), int(y_end) + 1)
    }


def update_velocity(velocity):
    x, y = velocity

    new_vel_x = x
    if x < 0:
        new_vel_x += 1
    elif x != 0:
        new_vel_x -= 1

    new_vel_y = y - 1

    return (new_vel_x, new_vel_y)


def target_passed(probe_loc, target):
    target_x = target["x"]
    target_y = target["y"]

    if probe_loc[0] > max(target_x):
        return True

    if probe_loc[1] < min(target_y):
        return True


def in_target(probe_loc, target):
    target_x = target["x"]
    target_y = target["y"]

    return probe_loc[0] in target_x and probe_loc[1] in target_y


def fire_probe(velocity, target):
    probe_loc = (0, 0)
    current_velocity = velocity

    probe_trajectory = []
    current_loc = probe_loc

    step = 0
    while not in_target(current_loc, target) and not target_passed(current_loc, target):
        v_x, v_y = current_velocity
        p_x, p_y = current_loc

        new_loc = (p_x + v_x, p_y + v_y)
        probe_trajectory.append(new_loc)
        current_loc = new_loc

        current_velocity = update_velocity(current_velocity)
        step += 1

    return in_target(current_loc, target), probe_trajectory


def find_valid_trajectories(target_area):
    valid_trajectories = []

    for x in range(1, 240):
        for y in range(-200, 200):
            velocity = (x, y)
            target_hit, trajectory = fire_probe(velocity, target_area)

            if target_hit:
                valid_trajectories.append(trajectory)

    return valid_trajectories


def find_highest_y_point(valid_trajectories):
    highest_y_point = 0
    for trajectory in valid_trajectories:
        max_y = max(map(lambda t: t[1], trajectory))

        if max_y > highest_y_point:
            highest_y_point = max_y

    return highest_y_point

if __name__ == '__main__':
    target_area = parse_target_area("target area: x=169..206, y=-108..-68")
    valid_trajectories = find_valid_trajectories(target_area)
    print(f"Day 17, part 1: {find_highest_y_point(valid_trajectories)}")
    print(f"Day 17, part 2: {len(valid_trajectories)}")