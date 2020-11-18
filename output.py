from statzcw import csvReader, zcount, zmean, zmode, \
    zmedian, zvariance, zstddev, zstderr, zcorr

csv_files = ['dataZero.csv', 'dataOne.csv', 'dataTwo.csv', 'dataThree.csv']
for f in csv_files:
    print('----------------------')
    print('File: ', f)
    print('----------------------')
    data = csvReader.read_csv(f)
    x = data[0]
    y = data[1]

    # x list
    print('x list')
    print('------')
    print('Count X: ', zcount.count(x))
    print('Mean X: ', zmean.mean(x))
    print('Median X ', zmedian.median(x))
    print('Mode X: ', zmode.mode(x))
    print('Variance X: ', zvariance.variance(x))
    print('Standard Deviation X: ', zstddev.stddev(x))
    print('Standard Error X: ', zstderr.stderr(x))

    # y list
    print('-------')
    print('y list:')
    print('-------')
    print('Count Y: ', zcount.count(y))
    print('Mean Y: ', zmean.mean(y))
    print('Median Y ', zmedian.median(y))
    print('Mode Y: ', zmode.mode(y))
    print('Variance Y: ', zvariance.variance(y))
    print('Standard Deviation Y: ', zstddev.stddev(y))
    print('Standard Error Y: ', zstderr.stderr(y))

    # Correlation
    print('---------------------')
    print('Correlation: ', zcorr.corr(x, y))
    print('')


