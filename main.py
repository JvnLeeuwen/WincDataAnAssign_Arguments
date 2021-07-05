# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting='Hello, <name>!'):
    """ Create a personalized greeting """
    index_name = greeting.find('<name>')
    return greeting[0: index_name] + name + greeting[(index_name + 6):]

def force(mass=0, body='earth'):
    """ Calculate the force working on a specified mass and planet"""
    grav_lookup={'sun':274,
                'jupiter':24.9,
                'neptune':11.2,
                'saturn':10.4,
                'earth':9.8,
                'uranus':8.9,
                'venus':8.9,
                'mars':3.7,
                'mercury':3.7,
                'moon':1.6,
                'pluto':0.6}
    return mass*grav_lookup[body]

def pull(m1, m2, d):
    """Calculate the pull between two masses at a specified distance"""
    G = 6.674*10**(-11)
    return G*m1*m2/d**2



