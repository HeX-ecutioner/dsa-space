import React from 'react';

export const Hero: React.FC = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        <div className="hero-icon">
          <img src="/favicon.png" alt="Logo" style={{ width: '2.5em', height: '2.5em' }} />
        </div>
        <h1 className="hero-title">DSA Interactive Workspace</h1>
        <p className="hero-subtitle">Select a topic, concept, or problem from the sidebar to begin your session.</p>
        <div className="hero-features">
          <div className="feature">
            <span className="feature-icon">📖</span>
            <span>Read deeply through the foundational concepts.</span>
          </div>
          <div className="feature">
            <span className="feature-icon">💻</span>
            <span>Study code solutions side-by-side.</span>
          </div>
          <div className="feature">
            <span className="feature-icon">🔍</span>
            <span>Instantly search structural patterns.</span>
          </div>
        </div>
      </div>
    </div>
  );
};
