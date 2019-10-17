# class Website: 
#     def __init__(self, title):
#         self.title = title

# ws = Website('My Website Title')
# print(ws.__dict__)
# ws_two = Website('Second Title')
# print(ws_two.__dict__)

class DifferentWebsite:
    title = 'My Class Title'

dw = DifferentWebsite()
print(dw.__dict__)

dw_two = DifferentWebsite()
print(dw_two.title)