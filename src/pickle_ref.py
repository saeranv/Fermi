import loadenv

import cPickle

def pickle(uwg):
    # create a binary file for serialized obj
    CURR_DIR = "C:\saeran\master\git\uwg\resources"

    pkl_file_path = os.path.join(CURR_DIR, 'uwg_heat_balance_bug.pkl')
    uwg_pickle = open(pkl_file_path, 'wb')

    # Pickle objects, protocol 1 b/c binary file
    cPickle.dump(uwg, uwg_pickle,1)

    uwg_pickle.close()

def unpickle(pkl_file_path):
    pkl_file = open(pkl_file_path, 'rb')  # open pickle file in binary form
    unpickled_object = cPickle.load(pkl_file)
    pkl_file.close()

    return unpickled_object


if __name__ == "__main__":
    fpath = "C:\\saeran\\master\\git\\uwg\\resources\\uwg_heat_balance_bug.pkl"
    unpkl_obj = unpickle(fpath)
    print unpkl_obj
    print("unpkl_obj from resources")
