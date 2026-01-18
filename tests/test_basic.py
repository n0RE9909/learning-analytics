import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import LearningAnalytics
import pandas as pd
import numpy as np

def test_learning_analytics_init():
    """Тест инициализации класса"""
    analyzer = LearningAnalytics()
    assert analyzer.data is None
    assert analyzer.predictions is None
    print("✅ test_learning_analytics_init passed")

def test_load_data():
    """Тест загрузки данных"""
    analyzer = LearningAnalytics()
    
    # Создаем тестовые данные
    test_data = pd.DataFrame({
        'student_id': ['TEST001', 'TEST002'],
        'assignment_avg': [80, 90],
        'quiz_avg': [85, 88],
        'midterm_score': [82, 92],
        'final_grade': [84, 93]
    })
    
    # Сохраняем во временный файл
    test_data.to_csv('test_data.csv', index=False)
    
    # Загружаем
    loaded_data = analyzer.load_data('test_data.csv')
    
    assert len(loaded_data) == 2
    assert 'student_id' in loaded_data.columns
    
    # Удаляем временный файл
    import os
    os.remove('test_data.csv')
    
    print("✅ test_load_data passed")

def test_analyze_performance():
    """Тест анализа данных"""
    analyzer = LearningAnalytics()
    
    # Создаем тестовые данные
    test_data = pd.DataFrame({
        'final_grade': [80, 90, 65, 95, 55]
    })
    analyzer.data = test_data
    
    stats = analyzer.analyze_performance()
    
    assert 'average_grade' in stats
    assert 'at_risk_count' in stats
    assert stats['at_risk_count'] == 2  # 65 и 55 < 70
    
    print("✅ test_analyze_performance passed")

def test_predict_grades():
    """Тест предсказания оценок"""
    analyzer = LearningAnalytics()
    
    # Создаем тестовые данные
    test_data = pd.DataFrame({
        'assignment_avg': [80, 90],
        'quiz_avg': [85, 88],
        'midterm_score': [82, 92]
    })
    analyzer.data = test_data
    
    predictions = analyzer.predict_grades()
    
    assert 'predicted_grade' in predictions.columns
    assert len(predictions) == 2
    
    # Проверяем расчет
    expected = 80*0.3 + 85*0.2 + 82*0.5
    assert abs(predictions.iloc[0]['predicted_grade'] - expected) < 0.01
    
    print("✅ test_predict_grades passed")

def run_all_tests():
    """Запуск всех тестов"""
    print("🧪 Запуск тестов Learning Analytics...")
    
    test_learning_analytics_init()
    test_load_data()
    test_analyze_performance()
    test_predict_grades()
    
    print("🎉 Все тесты пройдены успешно!")

if __name__ == "__main__":
    run_all_tests()
