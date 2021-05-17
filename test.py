test.describe("sample tests")

blinker = [[0,1,0],
           [0,1,0],
           [0,1,0]]
blinker_solution = [[0,0,0],
                    [1,1,1],
                    [0,0,0]]
                                      
glider =  [[1,0,0,0,0,0,0],
           [0,1,1,0,0,0,0],
           [1,1,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]
glider_solution = [[0,1,0,0,0,0,0],
                   [0,0,1,0,0,0,0],
                   [1,1,1,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0]]
test.it("blinker")
print(htmlize(blinker))
resp = next_gen(blinker)
test.expect(resp==blinker_solution, "Got<br/>" + htmlize(resp)  + "<br/>instead of<br/>" + htmlize(blinker_solution))

test.it("glider")
print(htmlize(glider))
resp = next_gen(glider)
test.expect(resp==glider_solution, "Got<br/>" + htmlize(resp)  + "<br/>instead of<br/>" + htmlize(glider_solution))
