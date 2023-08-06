from stdcomQt.stdcomQtC20 import *

one = 7
if one == 1 :
    print("one is : ", one)
    import matplotlib.pyplot as plt

    from sklearn import datasets

    digits = datasets.load_digits()
    print(digits.data)

    # Join the images and target labels in a list
    images_and_labels = list(zip(digits.images, digits.target))

    # for every element in the list
    for index, (image, label) in enumerate(images_and_labels[:8]):
        # initialize a subplot of 2X4 at the i+1-th position
        plt.subplot(2, 4, index + 1)
        # Display images in all subplots
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        # Add a title to each subplot
        plt.title('Training: ' + str(label))

    # Show the plot
    plt.show()

elif one == 2 :
    print("one is : ", one)
    from gekko import GEKKO as FirstClown
    import numpy as np
    import matplotlib.pyplot as plt

    m = FirstClown()
    tf = 40
    m.time = np.linspace(0, tf, 2 * tf + 1)
    step = np.zeros(2 * tf + 1)
    step[3:40] = 2.0
    print("step a", step)

    step[40:] = 5.0
    print("step b", step)

    # Controller model
    Kc = 15.0  # controller gain
    tauI = 2.0  # controller reset time
    tauD = 1.0  # derivative constant
    OP_0 = m.Const(value=0.0)  # OP bias
    OP = m.Var(value=0.0)  # controller output
    PV = m.Var(value=0.0)  # process variable
    SP = m.Param(value=step)  # set point
    Intgl = m.Var(value=0.0)  # integral of the error
    err = m.Intermediate(SP - PV)  # set point error
    m.Equation(Intgl.dt() == err)  # integral of the error
    m.Equation(OP == OP_0 + Kc * err + (Kc / tauI) * Intgl - PV.dt())

    # Process model
    Kp = 0.5  # process gain
    tauP = 40.0  # process time constant
    m.Equation(tauP * PV.dt() + PV == Kp * OP)

    m.options.IMODE = 4
    m.solve(disp=False)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(m.time, OP.value, 'b:', label='OP')
    plt.ylabel('Output')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(m.time, SP.value, 'k-', label='SP')
    plt.plot(m.time, PV.value, 'r--', label='PV')
    plt.xlabel('Time (sec)')
    plt.ylabel('Process')
    plt.legend()
    plt.show()

elif one == 3 :

    print("one is : ", one)
    import datetime
    import pandas_datareader.data as web
    import matplotlib.pyplot as plt
    from matplotlib import style

    # Adjusting the size of matplotlib
    import matplotlib as mpl


    class RealData :
        df = None
        name = None
        start = None
        stop = None

        def __init__(self, name : str = None, start : datetime.datetime = None, stop : datetime.datetime = None):

            self.df = None
            self.start = None
            self.stop = None

            if name is None :
                self.name = "spy"
            else:
                self.name = name

            if start is None :
                self.start = datetime.datetime(2020, 1, 1)
            else :
                self.start = start

            if stop is None :
                self.stop = datetime.datetime(2022, 11, 6)
            else:
                self.stop = stop

            self.df = web.DataReader("spy", 'yahoo', self.start, self.stop)

            print(self.df.tail())


    class RollingMean( ) :
        rd = None
        period = 30
        close_px = None
        mavg = None

        def __init__(self, rd: RealData, period : int = 30) :
            self.rd =  rd
            self.period = period
            self.close_px = self.rd.df['Adj Close']
            self.mavg = self.close_px.rolling(window=self.period).mean()


    class PlotMean( ) :
        rd = None
        rm = None

        def __init__(self, rd: RealData, rm : RollingMean ) :
            self.rd = rd
            self.rm = rm
            close_px = self.rm.close_px
            mavg = self.rm.mavg

            mpl.rc('figure', figsize=(8, 7))
            mpl.__version__

            # Adjusting the style of matplotlib
            style.use('ggplot')

            close_px.plot(label=self.rd.name)
            mavg.plot(label= 'mavg '+ str(self.rm.period))
            plt.legend()


            plt.show()


    class PlotRoR() :
        rd = None
        rm = None

        def __init__(self, rd: RealData, rm: RollingMean):
            self.rd = rd
            self.rm = rm
            close_px = self.rm.close_px

            rets = close_px / close_px.shift(1) - 1
            rets.plot(label='returns ' + self.rd.name )

            mpl.rc('figure', figsize=(8, 7))
            mpl.__version__

            # Adjusting the style of matplotlib
            style.use('ggplot')

            plt.plot(label=self.rd.name + " returns")

            plt.legend()
            plt.show()

    if __name__ == '__main__':
        rd = RealData()
        rm = RollingMean(rd)
        vm = PlotMean(rd,rm)
        pm = PlotRoR(rd,rm)

        #         pw = PlotRoR(rd,rm)

        while( 1) :
            print(".")

elif one == 4 :

    if __name__ == '__main__':
        import numpy as np

        import tensorflow as tf
        from tensorflow.python.keras import Sequential
        from tensorflow.python.keras.layers import Dense


        tf.random.set_seed(-1)

        l0 = Dense(units=1, input_shape=[1])

        model = Sequential([l0])
        model.compile(optimizer='sgd', loss='mean_squared_error')

        xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
        ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


        model.fit(xs, ys, epochs=500)

        print(model.predict([10.0]))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        s = l0.get_weights()
        print(s)  # print what the network has learned

        slope = s[0][0][0]
        intercept = s[1][0]

        for i in range(0,len(xs)) :
            x = xs[i]
            rv = (x * slope) + intercept

            print ( "x=", xs[i], ": y=", ys[i], ":  Resolved=", rv, ": Delta=", ys[i]-rv   )


elif one == 5 :

    if __name__ == '__main__':
        # Licensed under the Apache License, Version 2.0 (the "License")
        # you may not use this file except in compliance with the License.
        # You may obtain a copy of the License at

        # https://www.apache.org/licenses/LICENSE-2.0

        # Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an \"AS IS\" BASIS,
        # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        # See the License for the specific language governing permissions and
        # limitations under the License.
        import tensorflow as tf

        data = tf.keras.datasets.fashion_mnist

        (training_images, training_labels), (test_images, test_labels) = data.load_data()

        training_images = training_images / 255.0
        test_images = test_images / 255.0

        model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),
                                            tf.keras.layers.Dense(256, activation=tf.nn.relu),
                                            tf.keras.layers.Dropout(0.2),
                                            tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                            tf.keras.layers.Dropout(0.2),
                                            tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                            tf.keras.layers.Dropout(0.2),
                                            tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(training_images, training_labels, epochs=20)

        model.evaluate(test_images, test_labels)

        classifications = model.predict(test_images)
        print('xxxxxx', classifications[0])

        print('yyyyyy', test_labels[0])

elif one is 6 :

    if __name__ == '__main__':
        import tclab
        import time
        import numpy as np
        from simple_pid import PID
        import matplotlib.pyplot as plt

        # Create PID controller
        pid = PID(Kp=5.0, Ki=0.05, Kd=1.0, \
                  setpoint=50, sample_time=1.0, \
                  output_limits=(0, 100))

        n = 300
        tm = np.linspace(0, n - 1, n)
        T1 = np.zeros(n);
        Q1 = np.zeros(n)

        lab = tclab.TCLabModel()
        #lab = tclab.TCLab()

        for i in range(n):
            # read temperature
            T1[i] = lab.T1

            # PID control
            Q1[i] = pid(T1[i])
            lab.Q1(Q1[i])

            # print
            if i % 50 == 0:
                print('Time OP PV   SP')
            if i % 5 == 0:
                print(i, round(Q1[i], 2), T1[i], pid.setpoint)
            # wait sample time
            time.sleep(pid.sample_time)  # wait 1 sec

        lab.close()

        # Create Figure
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.grid()
        plt.plot([0, tm[-1] / 60.0], [50, 50], 'k-', label=r'$T_1$ SP')
        plt.plot(tm / 60.0, T1, 'r.', label=r'$T_1$ PV')
        plt.ylabel(r'Temp ($^oC$)')
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.grid()
        plt.plot(tm / 60.0, Q1, 'b-', label=r'$Q_1$')
        plt.ylabel(r'Heater (%)');
        plt.xlabel('Time (min)')
        plt.legend()
        plt.show()


elif one is 7 :

    if __name__ == '__main__':
        import tclab
        import time
        import numpy as np
        from simple_pid import PID
        import matplotlib.pyplot as plt

        # Create PID controller
        pid = PID(Kp=5.0, Ki=.05, Kd=0, \
                  setpoint=0, sample_time=1.0, \
                  output_limits=(0, 100))

        n = 300
        tm = np.linspace(0, n - 1, n)
        T1 = np.zeros(n);
        Q1 = np.zeros(n)

        lab = tclab.TCLabModel()
        #lab = tclab.TCLab()

        for i in range(n):
            # read temperature
            v = lab.T1 - 50.0

            T1[i] = v

            # PID control
            Q1[i] = pid(T1[i])
            lab.Q1(Q1[i])

            # print
            if i % 50 == 0:
                print('Time OP PV   SP')
            if i % 5 == 0:
                print(i, round(Q1[i], 2), T1[i], pid.setpoint)
            # wait sample time
            time.sleep(pid.sample_time)  # wait 1 sec


        lab.close()

        # Create Figure
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.grid()
        plt.plot([0, tm[-1] / 60.0], [50, 50], 'k-', label=r'$T_1$ SP')
        plt.plot(tm / 60.0, T1, 'r.', label=r'$T_1$ PV')
        plt.ylabel(r'Temp ($^oC$)')
        plt.legend()
        plt.subplot(2, 1, 2)
        plt.grid()
        plt.plot(tm / 60.0, Q1, 'b-', label=r'$Q_1$')
        plt.ylabel(r'Heater (%)');
        plt.xlabel('Time (min)')
        plt.legend()
        plt.show()

