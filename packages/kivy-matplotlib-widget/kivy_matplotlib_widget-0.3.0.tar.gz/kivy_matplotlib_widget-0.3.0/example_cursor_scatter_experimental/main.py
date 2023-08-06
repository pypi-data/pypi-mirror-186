from kivy.utils import platform

#avoid conflict between mouse provider and touch (very important with touch device)
#no need for android platform
if platform != 'android':
    from kivy.config import Config
    Config.set('input', 'mouse', 'mouse,disable_on_activity')

from kivy.lang import Builder
from kivy.app import App
from graph_generator import GraphGenerator

KV = '''
#:import MatplotFigureScatter graph_widget_scatter

Screen
    figure_wgt:figure_wgt
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint_y:0.2
            Button:
                text:"home"
                on_release:app.home()
            ToggleButton:
                group:'touch_mode'
                state:'down'
                text:"pan" 
                on_press:
                    app.set_touch_mode('pan')
                    self.state='down'
            ToggleButton:
                group:'touch_mode'
                text:"cursor"  
                on_press:
                    app.set_touch_mode('cursor')
                    self.state='down'                
        MatplotFigureScatter:
            id:figure_wgt
'''


class Test(App):
    lines = []

    def build(self):  
        self.screen=Builder.load_string(KV)
        return self.screen

    def on_start(self, *args):
        mygraph = GraphGenerator()
        
        self.screen.figure_wgt.figure = mygraph.fig
        self.screen.figure_wgt.scatter_label  = ['pt' + str(i) for i in mygraph.ptid]
        self.screen.figure_wgt.axes = mygraph.ax1
        self.screen.figure_wgt.xmin = mygraph.xmin
        self.screen.figure_wgt.xmax = mygraph.xmax
        self.screen.figure_wgt.ymin = mygraph.ymin
        self.screen.figure_wgt.ymax = mygraph.ymax
        # self.screen.figure_wgt.fast_draw = False #update axis during pan/zoom
        self.screen.figure_wgt.multi_xdata=True
        self.screen.figure_wgt.xsorted=False
        
        #register lines instance if need to be update
        self.lines.append(mygraph.line1)
        self.screen.figure_wgt.register_scatters(self.lines)
        # self.lines.append(mygraph.line2)
        
        self.screen.figure_wgt.register_lines([])

    def set_touch_mode(self,mode):
        self.screen.figure_wgt.touch_mode=mode

    def home(self):
        self.screen.figure_wgt.home()
        
Test().run()