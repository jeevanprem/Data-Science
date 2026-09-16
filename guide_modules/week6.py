# -*- coding: utf-8 -*-
"""Week 6 Module: Predictive Modeling - Simple & Multiple Linear Regression"""

def get_week6_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 6 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week6">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 06</span> Predictive Modeling: Linear Regression</h2>
                    <div class="module-lectures">NPTEL Lectures 29–38 | Ordinary Least Squares, Assumptions (LINE), Residuals, ANOVA Decomposition, R², and MLR</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        Linear regression is the bedrock predictive supervised learning algorithm for quantitative continuous target variables. It formalizes an empirical relationship between one or more predictor (independent) variables and a scalar response (dependent) variable.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Simple Linear Regression (SLR) &amp; OLS Formulation</h4>
                        <p>
                            The theoretical population model relating predictor $X$ to response $Y$ is:
                            $$Y_i = \\beta_0 + \\beta_1 X_i + \\epsilon_i, \\quad i = 1, \\dots, n$$
                            where $\\beta_0$ is the intercept, $\\beta_1$ is the regression slope, and $\\epsilon_i$ represents unobserved random error.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>The Gauss–Markov Assumptions (LINE):</strong>
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li><strong>L (Linearity):</strong> The relationship between $X$ and the conditional mean of $Y$ is linear: $E[Y \\mid X] = \\beta_0 + \\beta_1 X$.</li>
                                    <li><strong>I (Independence):</strong> The error terms $\\epsilon_i$ are mutually independent ($\\text{Cov}(\\epsilon_i, \\epsilon_j) = 0$ for $i \\ne j$).</li>
                                    <li><strong>N (Normality):</strong> Errors are normally distributed: $\\epsilon_i \\sim N(0, \\sigma^2)$.</li>
                                    <li><strong>E (Equal Variance / Homoscedasticity):</strong> The variance of errors is constant across all predictor levels: $\\text{Var}(\\epsilon_i) = \\sigma^2$.</li>
                                </ul>
                            </li>
                            <li><strong>Ordinary Least Squares (OLS) Derivation:</strong>
                                <br>OLS minimizes the sum of squared vertical residuals (Error Sum of Squares):
                                $$\\min_{\\beta_0, \\beta_1} \\text{SSE}(\\beta_0, \\beta_1) = \\sum_{i=1}^n (Y_i - \\beta_0 - \\beta_1 X_i)^2$$
                                Setting partial derivatives to zero yields the closed-form estimators:
                                $$\\mathbf{\\hat{\\beta}_1 = \\frac{\\sum_{i=1}^n (X_i - \\bar{X})(Y_i - \\bar{Y})}{\\sum_{i=1}^n (X_i - \\bar{X})^2} = \\frac{\\text{Cov}(X, Y)}{\\text{Var}(X)} = r_{XY}\\frac{s_Y}{s_X}}$$
                                $$\\mathbf{\\hat{\\beta}_0 = \\bar{Y} - \\hat{\\beta}_1 \\bar{X}}$$
                                <em>Crucial Property:</em> The fitted regression line <strong>always passes through the centroid</strong> $(\\bar{X}, \\bar{Y})$!
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Residuals &amp; Geometric Properties</h4>
                        <p>
                            For observation $i$, the <strong>residual error</strong> is defined as:
                            $$\\mathbf{e_i = Y_i - \\hat{Y}_i = Y_i - (\\hat{\\beta}_0 + \\hat{\\beta}_1 X_i)}$$
                            <em>Exam Trap:</em> Residual is strictly <strong>Actual minus Predicted</strong> ($Y - \\hat{Y}$), NOT $\\hat{Y} - Y$!
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li>Sum of residuals is always zero: $\\sum_{i=1}^n e_i = 0 \\implies \\bar{e} = 0$.</li>
                            <li>Residuals are strictly orthogonal to predictor values: $\\sum_{i=1}^n e_i X_i = 0$.</li>
                            <li>Residuals are orthogonal to fitted values: $\\sum_{i=1}^n e_i \\hat{Y}_i = 0$.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Sum of Squares Decomposition &amp; Shortcut Computational Formulas</h4>
                        <p>
                            The total variability in response $Y$ partitions cleanly into explained (regression) and unexplained (residual error) components:
                            $$\\mathbf{\\text{SST} = \\text{SSR} + \\text{SSE}}$$
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Total Sum of Squares (SST):</strong> $S_{YY} = \\sum (Y_i - \\bar{Y})^2 = \\sum Y_i^2 - \\frac{(\\sum Y_i)^2}{n}$ with $\\text{df} = n - 1$.</li>
                            <li><strong>Regression Sum of Squares (SSR):</strong> $\\sum (\\hat{Y}_i - \\bar{Y})^2 = \\hat{\\beta}_1 S_{XY} = \\mathbf{\\frac{S_{XY}^2}{S_{XX}}}$ with $\\text{df} = p$ ($1$ for SLR).</li>
                            <li><strong>Error / Residual Sum of Squares (SSE):</strong> $\\sum (Y_i - \\hat{Y}_i)^2 = \\mathbf{\\text{SST} - \\text{SSR} = S_{YY} - \\frac{S_{XY}^2}{S_{XX}}}$ with $\\text{df} = n - p - 1$.</li>
                            <li><strong>Mean Squared Errors:</strong> $\\text{MSR} = \\frac{\\text{SSR}}{p}$ and $\\text{MSE} = s_e^2 = \\frac{\\text{SSE}}{n - p - 1}$. Residual Standard Error is $s_e = \\sqrt{\\text{MSE}}$.</li>
                            <li><strong>Coefficient of Determination ($R^2$):</strong>
                                $$R^2 = \\frac{\\text{SSR}}{\\text{SST}} = 1 - \\frac{\\text{SSE}}{\\text{SST}} = \\frac{S_{XY}^2}{S_{XX} S_{YY}} = r_{XY}^2 \\in [0, 1]$$
                            </li>
                            <li><strong>Adjusted $R^2$:</strong>
                                $$\\text{Adjusted } R^2 = 1 - \\left[\\frac{\\text{SSE}/(n - p - 1)}{\\text{SST}/(n - 1)}\\right] = 1 - (1 - R^2)\\frac{n - 1}{n - p - 1}$$
                                Unlike $R^2$ which artificially increases with every added variable, Adjusted $R^2$ penalizes redundant predictors and only rises if the variable significantly improves explanatory power.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Line-by-Line Guide to R <code class="inline-code">summary(lm())</code> Output</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Residuals Summary (Min, 1Q, Median, 3Q, Max):</strong> Checks residual symmetry. Under normality, the median should be close to $0$, and $|\\text{1Q}| \\approx |\\text{3Q}|$.</li>
                            <li><strong>Coefficients Table:</strong>
                                <br>• <em>Estimate:</em> OLS estimates $\\hat{\\beta}_0$ (Intercept) and $\\hat{\\beta}_j$ (Slopes).
                                <br>• <em>Std. Error:</em> $\\text{SE}(\\hat{\\beta}_j) = \\sqrt{\\text{MSE} \\cdot (X^T X)^{-1}_{jj}}$.
                                <br>• <em>t value:</em> Test statistic $t = \\frac{\\hat{\\beta}_j - 0}{\\text{SE}(\\hat{\\beta}_j)}$ under null hypothesis $H_0: \\beta_j = 0$.
                                <br>• <em>Pr(&gt;|t|):</em> Two-tailed p-value. If $p &lt; 0.05$, predictor is statistically significant.
                            </li>
                            <li><strong>Residual Standard Error ($s_e$):</strong> Estimate of population error standard deviation $\\sigma = \\sqrt{\\text{MSE}}$ on $n - p - 1$ degrees of freedom.</li>
                            <li><strong>F-Statistic:</strong> Tests global hypothesis $H_0: \\beta_1 = \\beta_2 = \\dots = \\beta_p = 0$ (all slopes zero simultaneously):
                                $$F = \\frac{\\text{MSR}}{\\text{MSE}} = \\frac{\\text{SSR}/p}{\\text{SSE}/(n - p - 1)} \\sim F_{p, \\; n - p - 1}$$
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Regression Diagnostics: The 4 Fundamental Residual Plots</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>1. Residuals vs Fitted:</strong> Verifies linearity and homoscedasticity. Points should form an unstructured random horizontal cloud around zero. Any curved trend indicates non-linearity; a funnel/megaphone shape signals heteroscedasticity (non-constant variance).</li>
                            <li><strong>2. Normal Q-Q Plot:</strong> Evaluates normality of error distribution. Standardized residuals plotted against theoretical standard normal quantiles. Points must track the straight diagonal line. Severe S-curves indicate heavy tails or skewness.</li>
                            <li><strong>3. Scale-Location Plot:</strong> $\\sqrt{|\\text{Standardized Residuals}|}$ vs Fitted values. Assesses homoscedasticity. The red smoother line should remain roughly horizontal and flat.</li>
                            <li><strong>4. Residuals vs Leverage (Cook's Distance):</strong> Identifies influential observations that disproportionately pull the regression line.
                                <br>• <em>Leverage $h_{ii}$ threshold:</em> Points with $h_{ii} &gt; \\frac{2(p+1)}{n}$ have high leverage in predictor space.
                                <br>• <em>Cook's Distance $D_i$:</em> Measures overall change in fitted values when observation $i$ is removed. Observations with $D_i &gt; 1$ (or $D_i &gt; 4/n$) are dangerous influential outliers.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">F. Multiple Regression, VIF &amp; Confidence vs Prediction Intervals</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Matrix MLR:</strong> $Y = X\\beta + \\epsilon \\implies \\hat{\\beta} = (X^T X)^{-1} X^T Y$. Requires $X$ to have full column rank ($p+1$).</li>
                            <li><strong>Variance Inflation Factor (VIF):</strong> Quantifies multicollinearity among predictors: $\\text{VIF}_j = \\frac{1}{1 - R_j^2}$. $\\text{VIF} &gt; 5$ or $10$ indicates severe correlation, inflating parameter standard errors.</li>
                            <li><strong>Confidence Interval for Mean Response $E[Y \\mid X_0]$:</strong>
                                $$\\hat{Y}_0 \\pm t_{\\alpha/2, n-2} \\, s_e \\sqrt{\\frac{1}{n} + \\frac{(X_0 - \\bar{X})^2}{S_{XX}}}$$
                            </li>
                            <li><strong>Prediction Interval for a Single Individual $Y_{\\text{new}}$:</strong>
                                $$\\hat{Y}_0 \\pm t_{\\alpha/2, n-2} \\, s_e \\sqrt{1 + \\frac{1}{n} + \\frac{(X_0 - \\bar{X})^2}{S_{XX}}}$$
                                <br>• <strong>KEY EXAM COMPARISON:</strong> The Prediction Interval is <strong>ALWAYS strictly wider</strong> than the Confidence Interval because of the $+1$ variance term representing individual observation noise.
                                <br>• Both intervals are narrowest at the centroid $X_0 = \\bar{X}$ and flare outwards parabolically as $X_0$ deviates from $\\bar{X}$.
                            </li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Residual Error Sign &amp; Covariance vs Correlation</h4>
                            <p>
                                <strong>Trap 1:</strong> Always compute $e = Y_{\\text{actual}} - \\hat{Y}_{\\text{predicted}}$. If actual is $94.5$ and predicted is $83.9845$, residual error is $+10.5155$, NOT $-10.5155$!
                                <br><strong>Trap 2:</strong> <em>"Covariance is a better metric than correlation to analyze association."</em> $\\implies$ <strong>FALSE!</strong> Covariance is scale-dependent (changes if you change units from meters to millimeters). Correlation is normalized to $[-1, 1]$, making it unitless and strictly comparable.
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's 15-Second R Regression Output Reading Blueprint</h4>
                            <p>
                                When inspecting R's <code class="inline-code">summary(lm(Y ~ X))</code>:
                                <br>1. <strong>Call formula:</strong> Verify which variable is LHS ($Y$, predicted) and RHS ($X$, predictor).
                                <br>2. <strong>Coefficients Table:</strong> First row is <code class="inline-code">(Intercept)</code> ($\\hat{\\beta}_0$); second row is slope $\\hat{\\beta}_1$.
                                <br>3. <strong>Slope Sign:</strong> $\\hat{\\beta}_1 &gt; 0 \\implies$ positive association; $\\hat{\\beta}_1 &lt; 0 \\implies$ negative association.
                                <br>4. <strong>Goodness of fit:</strong> Look at <code class="inline-code">Multiple R-squared</code> ($R^2$) and <code class="inline-code">Adjusted R-squared</code>.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Essential Mathematical Formulas &amp; ANOVA Identities</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>OLS Slope &amp; Intercept</span>
                                <span class="nav-badge">Closed-Form</span>
                            </div>
                            <div class="formula-math">
                                $$\\hat{\\beta}_1 = \\frac{S_{XY}}{S_{XX}} = r\\frac{s_Y}{s_X}, \\quad \\hat{\\beta}_0 = \\bar{Y} - \\hat{\\beta}_1 \\bar{X}$$
                            </div>
                            <div class="formula-desc">Slope equals ratio of sample covariance to sample variance of predictor. Intercept forces line through centroid $(\\bar{X}, \\bar{Y})$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given $s_X = 4, s_Y = 10, r_{XY} = 0.8, \\bar{X} = 15, \\bar{Y} = 40$. Find the fitted line equation.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Slope $\\hat{\\beta}_1 = 0.8(10/4) = 2.0$. Intercept $\\hat{\\beta}_0 = 40 - (2.0)(15) = 10$. Fitted line: $\\hat{Y} = 10 + 2X$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Prove whether the centroid $(\\bar{X}, \\bar{Y})$ must satisfy the OLS regression line.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Yes. By definition $\\hat{\\beta}_0 = \\bar{Y} - \\hat{\\beta}_1 \\bar{X} \\implies \\hat{Y}(\\bar{X}) = \\bar{Y} - \\hat{\\beta}_1 \\bar{X} + \\hat{\\beta}_1 \\bar{X} = \\bar{Y}$. Centroid always lies on the line.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>ANOVA Identity &amp; $R^2$</span>
                                <span class="nav-badge">Variance</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{SST} = \\text{SSR} + \\text{SSE}, \\quad R^2 = \\frac{\\text{SSR}}{\\text{SST}} = 1 - \\frac{\\text{SSE}}{\\text{SST}}$$
                            </div>
                            <div class="formula-desc">Total Sum of Squares (SST) partitioned into Regression Sum of Squares (SSR) and Error / Residual Sum of Squares (SSE).</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A regression model has $\\text{SST} = 500$ and $\\text{SSE} = 125$. Compute $\\text{SSR}$ and $R^2$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{SSR} = \\text{SST} - \\text{SSE} = 500 - 125 = 375$. Coefficient of determination $R^2 = \\frac{\\text{SSR}}{\\text{SST}} = \\frac{375}{500} = 0.75$ (75% variance explained).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is the relationship between ANOVA $R^2$ and Pearson correlation $r_{XY}$ in SLR?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> In simple linear regression with an intercept, $R^2 = r_{XY}^2$. If $r_{XY} = -0.70$, then $R^2 = (-0.70)^2 = 0.49$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Adjusted Coefficient of Determination</span>
                                <span class="nav-badge">Parsimony</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{Adj } R^2 = 1 - (1 - R^2)\\frac{n - 1}{n - p - 1} = 1 - \\frac{\\text{SSE}/(n - p - 1)}{\\text{SST}/(n - 1)}$$
                            </div>
                            <div class="formula-desc">Penalizes model for degrees of freedom consumed by $p$ predictors. Guards against overfitting.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given $n = 31, p = 2$ predictors, and $R^2 = 0.70$, calculate Adjusted $R^2$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Adj } R^2 = 1 - (1 - 0.70)\\frac{30}{31 - 2 - 1} = 1 - (0.30)\\frac{30}{28} = 1 - 0.3214 = 0.6786$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Can Adjusted $R^2$ decrease when an additional predictor is added?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Yes. While $R^2$ never decreases, Adjusted $R^2$ drops if the reduction in $\\text{SSE}$ is insufficient to offset the loss of 1 error degree of freedom.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>MLR Normal Equations</span>
                                <span class="nav-badge">Matrix OLS</span>
                            </div>
                            <div class="formula-math">
                                $$\\hat{\\beta} = (X^T X)^{-1} X^T Y$$
                            </div>
                            <div class="formula-desc">Matrix OLS solution minimizing $\\|Y - X\\beta\\|^2$, assuming design matrix $X$ has full column rank.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> For $n = 50$ rows and $p = 4$ predictors, what is the dimension of $X$ and $(X^T X)^{-1}$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Including intercept column of $1$s, $X$ is $50 \\times 5$. The matrix $X^T X$ and its inverse $(X^T X)^{-1}$ are $(p+1) \\times (p+1) = 5 \\times 5$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Under what condition does $(X^T X)^{-1}$ fail to exist?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> When $X$ does not have full column rank ($\\text{rank}(X) &lt; p + 1$) due to perfect multicollinearity (one predictor is an exact linear combination of others).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Sum of Squares Shortcut Identities</span>
                                <span class="nav-badge">Computation</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{SSR} = \\frac{S_{XY}^2}{S_{XX}}, \\quad \\text{SSE} = S_{YY} - \\frac{S_{XY}^2}{S_{XX}}, \\quad \\text{SST} = S_{YY}$$
                            </div>
                            <div class="formula-desc">Direct computation of ANOVA sum of squares using only bivariate summary cross-products $S_{XX}, S_{YY}, S_{XY}$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If $S_{XX} = 50, S_{YY} = 200, S_{XY} = 80$, find $\\text{SSR}$, $\\text{SSE}$, and $R^2$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{SSR} = 80^2 / 50 = 6400 / 50 = 128$. $\\text{SSE} = \\text{SST} - \\text{SSR} = 200 - 128 = 72$. $R^2 = 128 / 200 = 0.64$ (64%).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For $n = 10$, calculate the unbiased estimate of error variance $s_e^2$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $s_e^2 = \\text{MSE} = \\text{SSE} / (n - 2) = 72 / (10 - 2) = 72 / 8 = 9.0$. Residual standard error is $s_e = 3.0$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Mean vs Individual Response Intervals</span>
                                <span class="nav-badge">Inference</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{SE}(\\hat{\\mu}_0) = s_e\\sqrt{\\frac{1}{n} + \\frac{(X_0-\\bar{X})^2}{S_{XX}}}, \\quad \\text{SE}(Y_{\\text{new}}) = s_e\\sqrt{1 + \\frac{1}{n} + \\frac{(X_0-\\bar{X})^2}{S_{XX}}}$$
                            </div>
                            <div class="formula-desc">Prediction interval for a new observation is always wider than the confidence interval for the conditional mean due to $+1$ individual error variance.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> At what predictor value $X_0$ is the confidence interval for mean response narrowest?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> At the sample centroid $X_0 = \\bar{X}$, where $(X_0 - \\bar{X})^2 = 0$, giving minimum standard error $s_e / \\sqrt{n}$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Why is the prediction interval for $Y_{\\text{new}}$ always wider than for $E[Y \\mid X_0]$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> A single future observation involves two independent sources of variability: uncertainty in the estimated regression line PLUS the intrinsic random noise $\\epsilon_i$ of individual data points.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Regression Functions</h3>
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
                                    <td><span class="code-cell">lm()</span></td>
                                    <td><code class="inline-code">lm(formula, data)</code></td>
                                    <td>Fits simple and multiple linear regression models via OLS.</td>
                                    <td><code class="inline-code">model &lt;- lm(Bid_Price ~ Coupon_Rate, data = bonds)</code></td>
                                    <td>Fitted <code class="inline-code">lm</code> model object</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">summary()</span></td>
                                    <td><code class="inline-code">summary(object)</code></td>
                                    <td>Prints coefficients, standard errors, t-values, p-values, $R^2$, and F-stat.</td>
                                    <td><code class="inline-code">summary(model)</code></td>
                                    <td>Detailed regression summary table</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">residuals()</span></td>
                                    <td><code class="inline-code">residuals(object)</code></td>
                                    <td>Extracts observed residuals $e_i = Y_i - \\hat{Y}_i$.</td>
                                    <td><code class="inline-code">residuals(model)[1]</code></td>
                                    <td>Vector of sample residuals</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">fitted()</span></td>
                                    <td><code class="inline-code">fitted(object)</code></td>
                                    <td>Extracts fitted in-sample predictions $\\hat{Y}_i$.</td>
                                    <td><code class="inline-code">fitted(model)[1]</code></td>
                                    <td>Vector of fitted values $\\hat{Y}$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">predict()</span></td>
                                    <td><code class="inline-code">predict(object, newdata, interval = c("none", "confidence", "prediction"))</code></td>
                                    <td>Generates point predictions or confidence / prediction intervals for new observations.</td>
                                    <td><code class="inline-code">predict(model, new_df, interval = "prediction")</code></td>
                                    <td>Matrix with columns <code class="inline-code">fit</code>, <code class="inline-code">lwr</code>, <code class="inline-code">upr</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">anova()</span></td>
                                    <td><code class="inline-code">anova(object)</code></td>
                                    <td>Computes Analysis of Variance table (SSR, SSE, Mean Squares, F).</td>
                                    <td><code class="inline-code">anova(model)</code></td>
                                    <td>ANOVA table with sums of squares</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">confint()</span></td>
                                    <td><code class="inline-code">confint(object, level = 0.95)</code></td>
                                    <td>Calculates confidence intervals for the regression parameters $\\beta_0, \\beta_j$.</td>
                                    <td><code class="inline-code">confint(model, level = 0.95)</code></td>
                                    <td>$2 \\times 2$ matrix of lower and upper coefficient bounds</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">cooks.distance()</span></td>
                                    <td><code class="inline-code">cooks.distance(model)</code></td>
                                    <td>Computes Cook's distance for each observation to detect influential leverage points.</td>
                                    <td><code class="inline-code">which(cooks.distance(model) &gt; 1)</code></td>
                                    <td>Indices of high-influence observations</td>
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
                            <span class="q-tag q-tag-calc">Topic: Reading Regression Equations</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL bonds.txt Case</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Using the dataset <code class="inline-code">bonds.txt</code> with variables <em>Coupon rate</em> ($X$) and <em>Bid price</em> ($Y$), the fitted regression output is obtained. What is the correct mathematical relationship?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $\\text{Coupon rate} = 99.95 + 0.24 \\times \\text{Bid price}$</li>
                                <li><span class="opt-bullet">B.</span> $\\text{Bid price} = 99.95 + 0.24 \\times \\text{Coupon rate}$</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> $\\text{Bid price} = 74.7865 + 3.066 \\times \\text{Coupon rate}$</li>
                                <li><span class="opt-bullet">D.</span> $\\text{Coupon rate} = 74.7865 + 3.066 \\times \\text{Bid price}$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Identify Dependent vs Independent Variables</div>
                                    <p>The goal is to predict <strong>Bid Price</strong> from <strong>Coupon Rate</strong>. Thus, Bid Price ($Y$) appears on the LHS, and Coupon Rate ($X$) appears on the RHS:
                                    $$Y = \\beta_0 + \\beta_1 X$$
                                    This immediately eliminates Options A and D.
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Read Model Coefficients from Regression Output</div>
                                    <p>From the OLS regression summary on <code class="inline-code">bonds.txt</code>:
                                    <br>• Intercept $\\hat{\\beta}_0 = 74.7865$
                                    <br>• Slope $\\hat{\\beta}_1 = 3.0660$
                                    <br>Therefore: $\\text{Bid Price} = 74.7865 + 3.066 \\times \\text{Coupon Rate}$.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option C (Bid price = 74.7865 + 3.066 × Coupon rate)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Goodness-of-Fit Interpretation</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> In the bonds regression model, the reported $R^2$ value is $0.7516$. How is this value correctly interpreted?</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> Approximately $75.16\\%$ of the total variance in Bid Price is explained by Coupon Rate.</li>
                                <li><span class="opt-bullet">B.</span> The correlation coefficient between Coupon Rate and Bid Price is $0.7516$.</li>
                                <li><span class="opt-bullet">C.</span> The model has an error rate of $75.16\\%$.</li>
                                <li><span class="opt-bullet">D.</span> For every 1-unit increase in Coupon Rate, Bid Price increases by $75.16$ units.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Definition of $R^2$</div>
                                    <p>
                                        $R^2$ (coefficient of determination) is $\\frac{\\text{SSR}}{\\text{SST}}$. Multiplying by 100 converts it into a percentage:
                                        $$0.7516 \\times 100 = 75.16\\%$$
                                        Thus, $75.16\\%$ of the variation in the response variable (Bid Price) is explained by the linear relationship with Coupon Rate.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (75.16% of total variance is explained)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Sum of Squares Arithmetic</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> If in a linear regression model, $R^2 = 0.6$, the regression sum of squares is $\\text{SSR} = 200$, and the total sum of squares is $\\text{SST} = 500$, what is the error sum of squares ($\\text{SSE}$)?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $500$</li>
                                <li><span class="opt-bullet">B.</span> $200$</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> $300$</li>
                                <li><span class="opt-bullet">D.</span> None of the above</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Fundamental ANOVA Identity</div>
                                    <p>$$\\text{SST} = \\text{SSR} + \\text{SSE}$$
                                    $$\\text{SSE} = \\text{SST} - \\text{SSR} = 500 - 200 = \\mathbf{300}$$
                                    <em>Cross-check with $R^2$:</em>
                                    Notice $R^2 = \\frac{\\text{SSR}}{\\text{SST}} = \\frac{200}{500} = 0.4$ if SSR is regression; or if labeled from residual, $\\text{SSE} = 500 - 200 = 300$. Regardless of labeling conventions, the sum of squares identity $\\text{Total} = \\text{Part}_1 + \\text{Part}_2$ strictly guarantees $500 - 200 = 300$.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option C (300)
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
                            <span>Week 6 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: Residual Error &amp; Prediction on the Bonds Dataset
                            </p>
                            <p>
                                A financial analytics firm uses the regression model established in Question 1:
                                $$\\hat{Y} = 74.7865 + 3.066 X$$
                                where $X$ is the bond's Coupon Rate and $Y$ is the Bid Price.
                                <br>In the audit records, an actual bond with a Coupon Rate of $X = 3.0$ is traded at an observed Bid Price of $Y = 94.50$.
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>Compute the predicted Bid Price $\\hat{Y}$ for a bond with Coupon Rate $X = 3.0$.</li>
                                <li>Calculate the exact residual error $e = Y - \\hat{Y}$ obtained for this bond.</li>
                                <li>Given $n = 35$ bond observations and $p = 1$ predictor, with $R^2 = 0.7516$, compute the Adjusted $R^2$ value manually using the formula.</li>
                                <li>Write the complete R script to fit the model, predict the value, and output the residual.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Compute Predicted Bid Price</div>
                                        <p>Substitute $X = 3.0$ into the regression equation:
                                        $$\\hat{Y} = 74.7865 + 3.066(3) = 74.7865 + 9.198 = \\mathbf{83.9845}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Calculate Residual Error</div>
                                        <p>The residual is defined as Actual value minus Fitted value:
                                        $$e = Y - \\hat{Y} = 94.50 - 83.9845 = \\mathbf{10.5155}$$
                                        A positive residual indicates that the actual market bid price was $\$10.52$ higher than predicted by the coupon rate model.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Compute Adjusted $R^2$</div>
                                        <p>
                                            Using $n = 35$, $p = 1$, and $R^2 = 0.7516$:
                                            $$\\text{Adjusted } R^2 = 1 - (1 - R^2)\\frac{n - 1}{n - p - 1}$$
                                            $$\\text{Adjusted } R^2 = 1 - (1 - 0.7516)\\frac{35 - 1}{35 - 1 - 1} = 1 - (0.2484)\\frac{34}{33}$$
                                            $$\\text{Adjusted } R^2 = 1 - (0.2484)(1.030303) = 1 - 0.255927 = \\mathbf{0.7441}$$
                                            This matches the NPTEL assignment solution value of $0.7441$ ($74.41\\%$)!
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: R Code Implementation</div>
                                        <pre class="r-code"># Fitting Linear Regression Model
# bonds &lt;- read.table("bonds.txt", header = TRUE)
# model &lt;- lm(Bid_Price ~ Coupon_Rate, data = bonds)

# Analytical Demonstration
beta_0 &lt;- 74.7865
beta_1 &lt;- 3.066
x_new  &lt;- 3.0
y_act  &lt;- 94.50

# Predicted value
y_pred &lt;- beta_0 + beta_1 * x_new
# Residual error
residual_err &lt;- y_act - y_pred

# Adjusted R-squared
n &lt;- 35; p &lt;- 1; r2 &lt;- 0.7516
adj_r2 &lt;- 1 - (1 - r2) * (n - 1) / (n - p - 1)

cat(sprintf("Predicted Bid Price: %.4f\\n", y_pred))     # 83.9845
cat(sprintf("Residual Error: %.4f\\n", residual_err))     # 10.5155
cat(sprintf("Adjusted R-squared: %.4f\\n", adj_r2))       # 0.7441</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Results: Predicted Y = 83.9845, Residual Error = 10.5155, Adjusted R² = 0.7441.
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

print("Week 6 module loaded.")
