# -*- coding: utf-8 -*-
"""Week 7 Module: Classification, Cross-Validation & Logistic Regression"""

def get_week7_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 7 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week7">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 07</span> Classification, Cross-Validation &amp; Logistic Regression</h2>
                    <div class="module-lectures">NPTEL Lectures 39–45 | Model Validation (LOOCV, k-Fold), Logistic Regression, Sigmoid, Odds, and Confusion Matrix</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        When the response variable is qualitative (categorical) rather than continuous, linear regression breaks down mathematically. Week 7 introduces the rigorous foundations of classification, resampling validation techniques, and the logistic regression model.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Bias–Variance Decomposition &amp; Cross-Validation Techniques</h4>
                        <p>
                            The expected test mean squared error of a predictive model decomposes into three non-negative components:
                            $$\\text{Expected Test MSE} = \\text{Bias}^2(\\hat{f}(x_0)) + \\text{Var}(\\hat{f}(x_0)) + \\sigma^2$$
                            where $\\sigma^2$ is irreducible error.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Crucial Conceptual Distinction:</strong> <em>Bias–Variance Trade-off is a theoretical principle</em> describing model flexibility vs error, <strong>NOT a cross-validation technique</strong>!</li>
                            <li><strong>The Three Formal Cross-Validation Techniques:</strong>
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li><strong>1. Validation Set Approach:</strong> Randomly divides data into a training set (e.g. 70%) and a validation/test set (30%). <em>Limitations:</em> High variability depending on the specific random split; overestimates test error because the model is trained on fewer observations.</li>
                                    <li><strong>2. $k$-Fold Cross-Validation:</strong> Randomly divides data into $k$ equal-sized folds. For each fold $j \\in \\{1, \\dots, k\\}$, the model is trained on the remaining $k-1$ folds and tested on fold $j$. The cross-validation error is:
                                        $$\\text{CV}_{(k)} = \\frac{1}{k}\\sum_{j=1}^k \\text{MSE}_j$$
                                        Typically $k = 5$ or $k = 10$. Provides an optimal balance between computational tractability, bias, and variance.
                                    </li>
                                    <li><strong>3. Leave-One-Out Cross-Validation (LOOCV):</strong> The extreme case where $k = n$ (sample size). Exactly one observation is left out for testing, while $n-1$ are used for training. Repeated $n$ times.
                                        <br>• <em>Advantages:</em> Completely deterministic (zero randomness in splitting); almost unbiased estimate of test error.
                                        <br>• <em>Disadvantages:</em> Computationally expensive ($n$ model fits); high variance among test error estimates due to highly correlated training sets.
                                    </li>
                                </ul>
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Classification vs Regression: Why Ordinary Linear Regression Fails</h4>
                        <p>
                            A <strong>classification problem</strong> predicts a qualitative categorical label $Y \\in \\{0, 1\\}$ or $\\{1, \\dots, C\\}$ (e.g. Patient Diagnosed with Disease: Yes/No; Rain Tomorrow: Yes/No).
                            <br>Ordinary linear regression fails for classification because:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li>1. <strong>Unbounded Predictions:</strong> Linear regression $\\hat{Y} = X\\beta$ produces values outside $[0, 1]$ ($&lt; 0$ or $&gt; 1$), violating the axioms of probability.</li>
                            <li>2. <strong>Heteroscedasticity:</strong> The error variance $\\text{Var}(Y \\mid X) = p(X)(1 - p(X))$ changes with $X$, violating the constant variance assumption.</li>
                            <li>3. <strong>Non-Normality of Residuals:</strong> Errors take on only two discrete values ($1 - p(X)$ or $-p(X)$), violating Gaussian error assumptions.</li>
                            <li>4. <strong>Arbitrary Metric Encoding:</strong> Assigning dummy numbers like $1, 2, 3$ to unordered categories creates artificial ordinal distances that bias the model.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. The Logistic Regression Model: Sigmoid, Odds, and Logit</h4>
                        <p>
                            Logistic regression directly models the conditional probability $p(X) = P(Y = 1 \\mid X)$:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>The Sigmoid / Logistic Function:</strong>
                                $$\\mathbf{p(X) = \\frac{e^{\\beta_0 + \\beta_1 X}}{1 + e^{\\beta_0 + \\beta_1 X}} = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 X)}} \\in (0, 1)}$$
                                S-shaped curve strictly bounded between 0 and 1.
                            </li>
                            <li><strong>Odds:</strong> The ratio of success probability to failure probability:
                                $$\\mathbf{\\text{Odds} = \\frac{p(X)}{1 - p(X)} = e^{\\beta_0 + \\beta_1 X} \\in (0, \\infty)}$$
                            </li>
                            <li><strong>Log-Odds (Logit Transformation):</strong>
                                $$\\mathbf{\\ln\\left(\\frac{p(X)}{1 - p(X)}\\right) = \\beta_0 + \\beta_1 X \\in (-\\infty, \\infty)}$$
                                The logit transformation linearizes the logistic relationship! A 1-unit increase in $X$ changes the log-odds by $\\beta_1$, and multiplies the odds by the factor $e^{\\beta_1}$ (Odds Ratio).
                            </li>
                            <li><strong>Maximum Likelihood Estimation (MLE):</strong> Logistic regression coefficients are fitted not via least squares, but by maximizing the Bernoulli joint likelihood function:
                                $$L(\\beta) = \\prod_{i=1}^n [p(x_i)]^{y_i} [1 - p(x_i)]^{1 - y_i}$$
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Classification Performance Assessment (Confusion Matrix)</h4>
                        <p>
                            Evaluating binary predictions against ground truth using a $2 \\times 2$ Confusion Matrix:
                        </p>
                        <div class="table-responsive" style="margin: 10px 0;">
                            <table class="academic-table" style="text-align: center;">
                                <thead>
                                    <tr>
                                        <th></th>
                                        <th>Predicted: Positive ($\hat{Y} = 1$)</th>
                                        <th>Predicted: Negative ($\hat{Y} = 0$)</th>
                                        <th>Total</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Actual: Positive ($Y = 1$)</strong></td>
                                        <td style="background: #f0fdf4; font-weight: 700; color: #166534;">True Positive (TP)</td>
                                        <td style="background: #fef2f2; font-weight: 700; color: #991b1b;">False Negative (FN) [Type II]</td>
                                        <td><strong>Actual Positives ($TP + FN$)</strong></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Actual: Negative ($Y = 0$)</strong></td>
                                        <td style="background: #fef2f2; font-weight: 700; color: #991b1b;">False Positive (FP) [Type I]</td>
                                        <td style="background: #f0fdf4; font-weight: 700; color: #166534;">True Negative (TN)</td>
                                        <td><strong>Actual Negatives ($TN + FP$)</strong></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Accuracy:</strong> $\\frac{TP + TN}{TP + TN + FP + FN} = \\frac{\\text{Correct Predictions}}{\\text{Total Population}}$.
                                <br>• <em>Error Rate:</em> $1 - \\text{Accuracy} = \\frac{FP + FN}{TP + TN + FP + FN}$.
                            </li>
                            <li><strong>Sensitivity (Recall / True Positive Rate - TPR):</strong>
                                $$\\mathbf{\\text{Sensitivity} = \\frac{TP}{TP + FN}}$$
                                Proportion of actual positive cases correctly identified. Crucial in disease diagnosis!
                            </li>
                            <li><strong>Specificity (True Negative Rate - TNR):</strong>
                                $$\\mathbf{\\text{Specificity} = \\frac{TN}{TN + FP}}$$
                                Proportion of actual negative cases correctly cleared.
                            </li>
                            <li><strong>False Positive Rate (FPR):</strong> $\\text{FPR} = 1 - \\text{Specificity} = \\frac{FP}{TN + FP}$ (type I error rate; false alarms).</li>
                            <li><strong>False Negative Rate (FNR):</strong> $\\text{FNR} = 1 - \\text{Sensitivity} = \\frac{FN}{TP + FN}$ (type II error rate; missed detections).</li>
                            <li><strong>Precision (Positive Predictive Value - PPV):</strong>
                                $$\\mathbf{\\text{Precision} = \\frac{TP}{TP + FP}}$$
                                Proportion of positive alarms that are truly positive.
                            </li>
                            <li><strong>Negative Predictive Value (NPV):</strong> $\\text{NPV} = \\frac{TN}{TN + FN}$.</li>
                            <li><strong>$F_1$-Score:</strong> Harmonic mean of Precision and Recall:
                                $$F_1 = 2 \\cdot \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2TP}{2TP + FP + FN} \\in [0, 1]$$
                                Preferred over accuracy on heavily imbalanced datasets (e.g., fraud detection where negatives are $99.9\\%$).
                            </li>
                            <li><strong>ROC Curve &amp; AUC:</strong> Receiver Operating Characteristic curve plots $\\text{Sensitivity}$ ($y$-axis) vs $1 - \\text{Specificity}$ ($x$-axis) across all possible probability classification thresholds $p^* \\in [0, 1]$. Area Under the Curve (AUC) ranges from $0.5$ (random guess) to $1.0$ (perfect discrimination).</li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: glm() Family &amp; predict() type Parameter</h4>
                            <p>
                                <strong>Trap 1:</strong> In R's <code class="inline-code">glm()</code>, the argument <code class="inline-code">family = binomial</code> (or <code class="inline-code">family = "binomial"</code>) is <strong>mandatory</strong> for logistic regression. If omitted, R fits a standard linear model (<code class="inline-code">family = gaussian</code>)!
                                <br><strong>Trap 2:</strong> To obtain predicted probabilities $P(Y=1|X) \\in [0, 1]$, you must write <code class="inline-code">predict(model, type = "response")</code>. Omitting <code class="inline-code">type = "response"</code> returns the linear log-odds (link scale: $\\beta_0 + \\beta_1 X$) which can be negative or greater than 1!
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's Confusion Matrix Denominator Rule</h4>
                            <p>
                                Never mix up metric denominators:
                                <br>• <strong>Sensitivity (Recall):</strong> Divisor is <em>Actual Positives</em> ($TP + FN$).
                                <br>• <strong>Specificity:</strong> Divisor is <em>Actual Negatives</em> ($TN + FP$).
                                <br>• <strong>Precision:</strong> Divisor is <em>Predicted Positives</em> ($TP + FP$).
                                <br>• <strong>Accuracy:</strong> Divisor is <em>Total Population</em> ($TP + TN + FP + FN$).
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Essential Mathematical Formulas &amp; Classification Metrics</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Sigmoid / Logistic Function</span>
                                <span class="nav-badge">Probability</span>
                            </div>
                            <div class="formula-math">
                                $$p(X) = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 X)}}$$
                            </div>
                            <div class="formula-desc">Maps any real-valued linear input $(-\\infty, \\infty)$ strictly into valid probability range $(0, 1)$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If logit $z = \\beta_0 + \\beta_1 X = -1.5 + 0.5(5) = 1.0$, find predicted probability $p$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $p = \\frac{1}{1 + e^{-1.0}} = \\frac{1}{1 + 0.3679} = \\frac{1}{1.3679} \\approx 0.7311$ (73.11% probability).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For what value of linear predictor $z$ is the predicted probability exactly $0.50$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\frac{1}{1 + e^{-z}} = 0.5 \\implies e^{-z} = 1 \\implies z = 0$. Decision boundary cutoff occurs where $\\beta_0 + \\beta_1 X = 0 \\implies X^* = -\\beta_0 / \\beta_1$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Odds &amp; Logit Transform</span>
                                <span class="nav-badge">Log-Odds</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{Odds} = \\frac{p}{1-p}, \\quad \\text{logit}(p) = \\ln\\left(\\frac{p}{1-p}\\right) = \\beta_0 + \\beta_1 X$$
                            </div>
                            <div class="formula-desc">Logit linearizes parameter estimation. Odds ratio $e^{\\beta_1}$ gives multiplicative odds increase per unit predictor change.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If an event has probability $p = 0.80$, compute its odds and logit.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Odds} = \\frac{0.80}{1 - 0.80} = \\frac{0.80}{0.20} = 4.0$ (4 to 1). $\\text{logit}(0.80) = \\ln(4.0) \\approx 1.3863$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If logistic slope $\\hat{\\beta}_1 = 0.693$, what is the odds ratio per unit increase in $X$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Odds Ratio} = e^{\\hat{\\beta}_1} = e^{0.693} \\approx 2.00$. Each 1-unit increase in $X$ doubles the odds of the target outcome.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Sensitivity (True Positive Rate)</span>
                                <span class="nav-badge">Recall</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{TPR} = \\frac{TP}{TP + FN}$$
                            </div>
                            <div class="formula-desc">Ability of model to detect actual positives without missing true diseased/target cases.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A test on 100 sick patients identifies 85 correctly ($TP = 85$) and misses 15 ($FN = 15$). Find Sensitivity.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Sensitivity} = \\frac{85}{85 + 15} = \\frac{85}{100} = 0.85$ (85% recall).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If a naive classifier predicts ALL cases as Positive, what are its Sensitivity and Specificity?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> With $FN = 0$, $\\text{Sensitivity} = \\frac{TP}{TP + 0} = 1.00$ (100%). But $TN = 0$, so $\\text{Specificity} = 0$, giving $\\text{FPR} = 1 - 0 = 1.00$ (100% false alarms).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Specificity (True Negative Rate)</span>
                                <span class="nav-badge">Selectivity</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{TNR} = \\frac{TN}{TN + FP}$$
                            </div>
                            <div class="formula-desc">Ability of model to correctly clear non-target/healthy cases. False Positive Rate is $1 - \\text{Specificity}$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Out of 200 healthy patients, 180 test negative ($TN = 180$) and 20 test positive ($FP = 20$). Compute Specificity and FPR.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Specificity} = \\frac{180}{180 + 20} = 0.90$ (90%). False Positive Rate $= 1 - \\text{Specificity} = 1 - 0.90 = 0.10$ (10%).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What are the axes of a Receiver Operating Characteristic (ROC) curve?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> The vertical $y$-axis is Sensitivity (True Positive Rate: $\\frac{TP}{TP + FN}$), and the horizontal $x$-axis is $1 - \\text{Specificity}$ (False Positive Rate: $\\frac{FP}{TN + FP}$).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>$k$-Fold Cross-Validation Error</span>
                                <span class="nav-badge">Resampling</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{CV}_{(k)} = \\frac{1}{k}\\sum_{j=1}^k \\text{MSE}_j$$
                            </div>
                            <div class="formula-desc">Averages validation errors across $k$ non-overlapping folds. Provides an almost unbiased estimate of out-of-sample test error.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> In a 5-fold CV, MSEs on the 5 validation folds are $12, 16, 14, 18, 15$. Find $\\text{CV}_{(5)}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{CV}_{(5)} = \\frac{12 + 16 + 14 + 18 + 15}{5} = \\frac{75}{5} = 15.0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Why is $k$-fold cross-validation superior to a single validation split?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Every sample observation is used for testing exactly once. It avoids high dependency on an arbitrary single split and uses $(k-1)/k$ of the data for training.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>$F_1$-Score (Harmonic Mean)</span>
                                <span class="nav-badge">Imbalanced Data</span>
                            </div>
                            <div class="formula-math">
                                $$F_1 = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2TP}{2TP + FP + FN}$$
                            </div>
                            <div class="formula-desc">Harmonic mean balances Precision and Recall, heavily penalizing models that ignore either metric on skewed distributions.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A classifier has $\\text{Precision} = 0.80$ and $\\text{Recall} = 0.60$. Calculate $F_1$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $F_1 = 2 \\cdot \\frac{0.80 \\times 0.60}{0.80 + 0.60} = \\frac{0.96}{1.40} \\approx 0.6857$. (Harmonic mean is pulled toward the lower metric).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $TP = 40, FP = 10, FN = 10, TN = 140$, find the $F_1$-score.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $F_1 = \\frac{2(40)}{2(40) + 10 + 10} = \\frac{80}{100} = 0.80$.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Classification Functions</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Syntax</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Description &amp; Operation</th>
                                    <th>Practical Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">glm()</span></td>
                                    <td><code class="inline-code">glm(formula, data, family = binomial)</code></td>
                                    <td>Fits Generalized Linear Models. <code class="inline-code">family = binomial</code> specifies logistic link.</td>
                                    <td><code class="inline-code">glm(disease ~ age + bmi, family = binomial, data = df)</code></td>
                                    <td>Fitted logistic regression object</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">predict()</span></td>
                                    <td><code class="inline-code">predict(object, newdata, type = "response")</code></td>
                                    <td>Outputs predicted probabilities $P(Y=1|X) \\in [0, 1]$.</td>
                                    <td><code class="inline-code">predict(log_fit, type = "response")</code></td>
                                    <td>Vector of probabilities</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">table()</span></td>
                                    <td><code class="inline-code">table(Actual = y, Predicted = pred &gt; 0.5)</code></td>
                                    <td>Constructs empirical $2 \\times 2$ Confusion Matrix.</td>
                                    <td><code class="inline-code">table(y, pred &gt; 0.5)</code></td>
                                    <td>Contingency table of TP, FP, FN, TN</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">is.na()</span></td>
                                    <td><code class="inline-code">is.na(x)</code></td>
                                    <td>Checks for missing values (<code class="inline-code">NA</code>) across rows/columns.</td>
                                    <td><code class="inline-code">sum(is.na(df))</code></td>
                                    <td>Total count of missing elements</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">dim()</span></td>
                                    <td><code class="inline-code">dim(x)</code></td>
                                    <td>Retrieves dimensions (rows, columns) of a data frame or matrix.</td>
                                    <td><code class="inline-code">dim(iris)</code></td>
                                    <td><code class="inline-code">c(150, 5)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">cv.glm()</span></td>
                                    <td><code class="inline-code">boot::cv.glm(data, glmfit, K = 10)</code></td>
                                    <td>Calculates $k$-fold cross-validation or LOOCV estimate of prediction error.</td>
                                    <td><code class="inline-code">library(boot); cv.glm(df, fit, K=10)$delta[1]</code></td>
                                    <td>Cross-validation MSE error estimate</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">prop.table()</span></td>
                                    <td><code class="inline-code">prop.table(x, margin = NULL)</code></td>
                                    <td>Expresses table entries as proportions of marginal or total sums.</td>
                                    <td><code class="inline-code">prop.table(table(y, pred &gt; 0.5))</code></td>
                                    <td>Normalized confusion matrix proportion table</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Cross-Validation vs Bias-Variance</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Which among the following is <strong>NOT</strong> a type of cross-validation technique?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> LOOCV (Leave-One-Out Cross-Validation)</li>
                                <li><span class="opt-bullet">B.</span> $k$-fold cross-validation</li>
                                <li><span class="opt-bullet">C.</span> Validation set approach</li>
                                <li class="correct-option"><span class="opt-bullet">D.</span> Bias–variance trade-off</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Conceptual Classification</div>
                                    <p>
                                        • <strong>LOOCV</strong>, <strong>$k$-fold cross-validation</strong>, and the <strong>validation set approach</strong> are algorithmic data-resampling techniques used to estimate out-of-sample generalization error.
                                        <br>• In contrast, <strong>Bias–variance trade-off</strong> is a fundamental mathematical property of statistical models describing the balance between approximation error and estimation variance. It is a concept, not a validation resampling protocol!
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option D (Bias-variance trade-off)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Classification vs Regression Problems</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> Which among the following are <strong>classification problems</strong>? (Select all that apply.)</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> Predicting the average rainfall in a given month.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> Predicting whether a patient is diagnosed with a disease or not.</li>
                                <li><span class="opt-bullet">C.</span> Predicting the market sales price of a residential house.</li>
                                <li class="correct-option"><span class="opt-bullet">D.</span> Predicting whether it will rain or not tomorrow.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Analysis of Response Variable Types</div>
                                    <p>
                                        • <strong>Option A:</strong> Average rainfall is quantitative continuous (e.g. $124.5\\text{ mm}$) $\\implies$ <strong>Regression</strong>.
                                        <br>• <strong>Option B:</strong> Disease diagnosis is discrete binary ($1 = \\text{Disease}, 0 = \\text{Healthy}$) $\\implies$ <strong>Classification</strong>.
                                        <br>• <strong>Option C:</strong> House price is continuous dollar currency $\\implies$ <strong>Regression</strong>.
                                        <br>• <strong>Option D:</strong> Rain tomorrow is binary ($1 = \\text{Yes}, 0 = \\text{No}$) $\\implies$ <strong>Classification</strong>.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answers: Options B and D
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Confusion Matrix Metric Calculation</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> A classification model is tested on $200$ patients. The confusion matrix results in:
                            <br>$$\\text{True Positives (TP)} = 95, \\quad \\text{False Positives (FP)} = 5$$
                            $$\\text{False Negatives (FN)} = 0, \\quad \\text{True Negatives (TN)} = 100$$
                            Calculate the <strong>Sensitivity</strong> and <strong>Accuracy</strong> of this diagnostic model.</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> Sensitivity $= 1.00$ ($100\\%$); Accuracy $= 0.975$ ($97.5\\%$)</li>
                                <li><span class="opt-bullet">B.</span> Sensitivity $= 0.95$ ($95\\%$); Accuracy $= 0.95$ ($95\\%$)</li>
                                <li><span class="opt-bullet">C.</span> Sensitivity $= 0.55$ ($55\\%$); Accuracy $= 0.95$ ($95\\%$)</li>
                                <li><span class="opt-bullet">D.</span> Sensitivity $= 0.95$ ($95\\%$); Accuracy $= 1.00$ ($100\\%$)</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Compute Sensitivity (Recall)</div>
                                    <p>$$\\text{Sensitivity} = \\frac{TP}{TP + FN} = \\frac{95}{95 + 0} = \\frac{95}{95} = \\mathbf{1.00 \\quad (100\\%)}$$
                                    Because $FN = 0$, every single diseased patient was correctly detected!
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Compute Overall Accuracy</div>
                                    <p>$$\\text{Accuracy} = \\frac{TP + TN}{TP + TN + FP + FN} = \\frac{95 + 100}{95 + 100 + 5 + 0} = \\frac{195}{200} = \\mathbf{0.975 \\quad (97.5\\%)}$$
                                    <em>Note on NPTEL variant:</em> If $TP = 95, FP = 5, FN = 5, TN = 95$, Accuracy $= \\frac{190}{200} = 0.95$.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (Sensitivity = 1.00, Accuracy = 0.975)
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 7 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: End-to-End Logistic Regression &amp; Odds Multiplier
                            </p>
                            <p>
                                An epidemiologist fits a simple logistic regression model to predict the presence of cardiovascular disease ($Y = 1$ if diseased, $Y = 0$ if healthy) from blood cholesterol level $X$ (in tens of mg/dL):
                                $$\\ln\\left(\\frac{p(X)}{1 - p(X)}\\right) = -3.5 + 0.8 X$$
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>Compute the predicted disease probability $p(X)$ for a patient with cholesterol level $X = 5.0$.</li>
                                <li>By what multiplicative factor do the odds of having the disease increase for every 1-unit increase in $X$?</li>
                                <li>At a decision threshold of $\\tau = 0.5$, classify the patient as Diseased or Healthy.</li>
                                <li>Suppose on a validation set of $n = 100$ patients, the confusion matrix yields $TP = 42$, $FP = 8$, $FN = 6$, $TN = 44$. Calculate the <strong>Accuracy</strong>, <strong>Sensitivity</strong>, <strong>Specificity</strong>, and <strong>Precision</strong>.</li>
                                <li>Write the R code to execute this logistic regression analysis using <code class="inline-code">glm()</code>.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Compute Probability for $X = 5.0$</div>
                                        <p>First calculate the logit (linear predictor):
                                        $$z = \\beta_0 + \\beta_1 X = -3.5 + 0.8(5.0) = -3.5 + 4.0 = \\mathbf{0.5}$$
                                        Now apply the sigmoid function:
                                        $$p(5.0) = \\frac{1}{1 + e^{-0.5}} = \\frac{1}{1 + 0.60653} = \\frac{1}{1.60653} \\approx \\mathbf{0.6225 \\quad (62.25\\%)}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Odds Ratio Multiplier</div>
                                        <p>
                                            In logistic regression, the odds multiply by $e^{\\beta_1}$ for each 1-unit increase in $X$:
                                            $$\\text{Odds Ratio} = e^{\\beta_1} = e^{0.8} \\approx \\mathbf{2.2255}$$
                                            Thus, for every 1-unit increase in cholesterol, the odds of disease increase by approximately $122.55\\%$ (multiplied by $\\approx 2.23$).
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Classification Decision</div>
                                        <p>Since $p(5.0) = 0.6225 &gt; \\tau = 0.50$, the patient is classified as <strong>Diseased ($\hat{Y} = 1$)</strong>.</p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: Validation Set Performance Metrics</div>
                                        <p>Given $TP = 42, FP = 8, FN = 6, TN = 44$ (Total $= 100$):
                                        <br>• $\\text{Accuracy} = \\frac{TP + TN}{\\text{Total}} = \\frac{42 + 44}{100} = \\frac{86}{100} = \\mathbf{0.86 \\quad (86.0\\%)}$
                                        <br>• $\\text{Sensitivity} = \\frac{TP}{TP + FN} = \\frac{42}{42 + 6} = \\frac{42}{48} = \\mathbf{0.875 \\quad (87.5\\%)}$
                                        <br>• $\\text{Specificity} = \\frac{TN}{TN + FP} = \\frac{44}{44 + 8} = \\frac{44}{52} \\approx \\mathbf{0.8462 \\quad (84.62\\%)}$
                                        <br>• $\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{42}{42 + 8} = \\frac{42}{50} = \\mathbf{0.840 \\quad (84.0\\%)}$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 5: Complete R Script</div>
                                        <pre class="r-code"># Fitting Logistic Regression
# model &lt;- glm(disease ~ cholesterol, data = patient_data, family = binomial)

# Mathematical Verification
beta_0 &lt;- -3.5
beta_1 &lt;- 0.8
x_val  &lt;- 5.0

# Linear Predictor &amp; Probability
z &lt;- beta_0 + beta_1 * x_val
prob &lt;- 1 / (1 + exp(-z))
odds_ratio &lt;- exp(beta_1)

cat(sprintf("Logit z: %.2f\\n", z))                    # 0.50
cat(sprintf("Predicted Probability: %.4f\\n", prob))  # 0.6225
cat(sprintf("Odds Ratio Multiplier: %.4f\\n", odds_ratio)) # 2.2255

# Metrics
TP &lt;- 42; FP &lt;- 8; FN &lt;- 6; TN &lt;- 44
cat("Accuracy:", (TP + TN) / 100, "\\n")      # 0.86
cat("Sensitivity:", TP / (TP + FN), "\\n")    # 0.875
cat("Specificity:", round(TN / (TN + FP), 4), "\\n") # 0.8462
cat("Precision:", TP / (TP + FP), "\\n")      # 0.84</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Summary: p(5.0) = 0.6225 (Class: Diseased); Odds multiplier = 2.2255; Accuracy = 86%, Sensitivity = 87.5%.
                                    </div>
                                </div>
                            </details>
                        </div>
                    </div>
                </section>
            </div>
        </article>
        <div class="page-break"></div>
"""

print("Week 7 module loaded.")
