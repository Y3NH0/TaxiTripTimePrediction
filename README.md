# TaxiTripTimePrediction
* Kaggle Competition: [ECML/PKDD 15: Taxi Trip Time Prediction (II)](https://www.kaggle.com/competitions/pkdd-15-taxi-trip-time-prediction-ii)

# Result.
* private score / public score : 0.6856 / 0.7619
* feature set.
    - CALL_TYPE_STAND: combine CALL_TYPE and ORIGIN_STAND, one-hot encoding
    - MONTH: one-hot encoding
    - HOUR_GROUP: one-hot encoding
    - WEEKDAY_GROUP: one-hot encoding
    - StartCluster: frequency encoding
    - EndCluster: frequency encoding