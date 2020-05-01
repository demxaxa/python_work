#3-5

guess_list = ['ahmed','saber','mansour']

guess_list.pop()
guess_list.append('abdelkader')

print("I have found a bigger dinner table.")
guess_list.insert(0,'mansour')
guess_list.insert(2, 'cena')
guess_list.append('messi')

print("\nDear " + guess_list[0].title() + ", you have been invited to dinner.")
print("Dear " + guess_list[1].title() + ", you have been invited to dinner.")
print("Dear " + guess_list[3].title() + ", you have been invited to dinner.")
print("Dear " + guess_list[4].title() + ", you have been invited to dinner.")
print("Dear " + guess_list[5].title() + ", you have been invited to dinner.")
