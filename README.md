# Datathon 2024

## Competition
- **Platform:** Kaggle
- **Link:** [Datathon 2024](https://www.kaggle.com/competitions/datathon-2024/overview)
- **Tür:** Regresyon

## Model and Performance

### Model
XGBRegressor ile aşağıdaki hiperparametreler kullanılmıştır:

```python
XGBRegressor(
    objective='reg:squarederror',
    subsample=1.0,
    reg_lambda=3,
    reg_alpha=0.1,
    n_estimators=100,
    min_child_weight=5,
    max_depth=10,
    learning_rate=0.1,
    gamma=0.1,
    colsample_bytree=0.8,
    nthread=-1
)
```

### Performance
- **Metric:** RMSE (Root Mean Squared Error)
- **Score:** 6.73
