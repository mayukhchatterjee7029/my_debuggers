def create_clf_plots(model, X_train, X_val, y_train, y_val, model_name='Model', y_pred=None):
    """
    Create confusion matrix and learning curve plots for classification models
    
    Parameters:
    -----------
    model : sklearn classifier
        Trained classification model
    X_train : array-like
        Training features
    X_val : array-like
        Validation features  
    y_train : array-like
        Training labels
    y_val : array-like
        Validation labels
    model_name : str, default='Model'
        Name of the model for plot title
    y_pred : array-like, optional
        Predictions on validation set. If None, will be computed.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.model_selection import learning_curve
    
    if y_pred is None:
        y_pred = model.predict(X_val)
    
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle(f'{model_name} Classification Results', fontsize=16, fontweight='bold')
    
    # 1. Confusion Matrix
    cm = confusion_matrix(y_val, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title('Confusion Matrix')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('Actual')
    axes[0].set_xticklabels(['False', 'True'])
    axes[0].set_yticklabels(['False', 'True'])
    
    # 2. Learning Curve
    train_sizes, train_scores, val_scores = learning_curve(
        model, X_train, y_train, cv=5, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10))
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)
    
    axes[1].plot(train_sizes, train_mean, 'o-', color='blue', label='Training Score')
    axes[1].fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color='blue')
    axes[1].plot(train_sizes, val_mean, 'o-', color='red', label='Validation Score')
    axes[1].fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1, color='red')
    axes[1].set_xlabel('Training Set Size')
    axes[1].set_ylabel('Accuracy Score')
    axes[1].set_title('Learning Curve')
    axes[1].legend(loc='best')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print classification report
    print("Classification Report:")
    print("=" * 50)
    print(classification_report(y_val, y_pred))
