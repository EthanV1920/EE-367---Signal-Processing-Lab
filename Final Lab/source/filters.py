from scipy.signal import sosfilt #, butter   could be used to make butterworth filters using some other data from the matlab file
                                 # but it seems like more work than it's worth, lets see how these pan out first

def BP697(x):
    sos = [[1, 0, -1, 1, -0.881385021996587, 0.911473662795519]]
    scale_values = [0.0442631686022406, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP770(x):
    sos = [[1, 0, -1, 1, -0.666157014109844, 0.883665323160146]]
    scale_values = [0.0581673384199269, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP852(x):
    sos = [[1, 0, -1, 1, -0.431733010683812, 0.911473662795518]]
    scale_values = [0.044263168602241, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP941(x):
    sos = [[1, 0, -1, 1, -0.17735608093889, 0.883665323160146]]
    scale_values = [0.058167338419927, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP1209(x):
    sos = [[1, 0, -1, 1, 0.610453230045989, 0.883665323160146]]
    scale_values = [0.058167338419927, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP1336(x):
    sos = [[1, 0, -1, 1, 0.959337037818403, 0.883665323160145]]
    scale_values = [0.0581673384199272, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP1477(x):
    sos = [[1, 0, -1, 1, 1.2683561909662, 0.883665323160146]]
    scale_values = [0.058167338419927, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

def BP1633(x):
    sos = [[1, 0, -1, 1, 1.59121640388426, 0.883665323160147]]
    scale_values = [0.0581673384199265, 1]
    sos = [sos[i] / scale_values for i in range(len(sos))]  # Normalize SOS coefficients
    output_signal = sosfilt(sos, x)
    return output_signal

#theoretically this should condense the above functions into one, but it is untested may not work
#
# def apply_filter(x, sos_values, scale_values):
#     sos = [sos_values[i] / scale_values for i in range(len(sos_values))]  # Normalize SOS coefficients
#     output_signal = sosfilt(sos, x)
#     return output_signal

# filters = {
#     'BP697': [[1, 0, -1, 1, -0.881385021996587, 0.911473662795519], [0.0442631686022406, 1]],
#     'BP770': [[1, 0, -1, 1, -0.666157014109844, 0.883665323160146], [0.0581673384199269, 1]],
#     'BP852': [[1, 0, -1, 1, -0.431733010683812, 0.911473662795518], [0.044263168602241, 1]],
#     'BP941': [[1, 0, -1, 1, -0.17735608093889, 0.883665323160146], [0.058167338419927, 1]],
#     'BP1209': [[1, 0, -1, 1, 0.610453230045989, 0.883665323160146], [0.058167338419927, 1]],
#     'BP1336': [[1, 0, -1, 1, 0.959337037818403, 0.883665323160145], [0.0581673384199272, 1]],
#     'BP1477': [[1, 0, -1, 1, 1.2683561909662, 0.883665323160146], [0.058167338419927, 1]],
#     'BP1633': [[1, 0, -1, 1, 1.59121640388426, 0.883665323160147], [0.0581673384199265, 1]]
#     }

# def filter_signal(filter_name, x)):
#     sos_values, scale_values = filters[filter_name]
#     return apply_filter(x, sos_values, scale_values