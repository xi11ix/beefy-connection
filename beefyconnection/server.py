import cherrypy
import argparse

from bc import BeefyUser, BeefyPic, BeefyDisplay,BeefyConfig, BeefyConnection

def main():
    parser=argparse.ArgumentParser(description='Beefy Connection!!!')
    parser.add_argument('-c', '--config', dest='config',
                        default='beefy-connection.conf')
    parser.add_argument('-d', '--database', dest='database')
    args = parser.parse_args()
    bc_config=BeefyConfig(args)

    cherrypy.tree.mount(
        BeefyUser(bc_config), '/bc/submit',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        BeefyPic(), '/bc/pic',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        BeefyDisplay(),'/',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )


    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()

