from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to  list blogs, "r" to read one, "p" to create a post, "q" to quit'
POST_TEMPLATE = '''
--- {} ---

{}

'''

blogs = dict() # blog_name : Blog object


def menu():
    # Show the user available logs
    # Let the user make a choice
    # Do sth with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_blog()
        selection = input(MENU_PROMPT)


def print_blogs():
    # Print the available blogs
    print("Blogs!")
    for key, blog in blogs.items():
        print(f'- {blog}')


def ask_create_blog():
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input('Enter the blog title you want to read: ')

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Enter the blog title you want to write post in: ')
    title = input('Enter you post title: ')
    content = input('Enter your post content: ')

    blogs[blog_name].create_post(title, content)
