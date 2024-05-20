class StudentSandwich:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # this works because it uses two counters to keep track of the number of students who prefer sandwiches with 0 and 1
        # if the number of students who prefer sandwiches with 0 is greater than 0, remove the first sandwich from the list of sandwiches
        # if the sandwich is 0, remove the first student from the list of students
        # if the sandwich is not 0, append the first student to the end of the list of students
        # if the number of students who prefer sandwiches with 0 is 0, return the length of the list of students
        count = [0, 0]
        for s in students:
            count[s] += 1
        for i in range(len(sandwiches)):
            if count[sandwiches[i]] > 0:
                count[sandwiches[i]] -= 1
            else:
                return len(sandwiches) - i
        return 0


if __name__ == '__main__':
    ss = StudentSandwich()
    print(ss.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # 0
