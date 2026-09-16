# -*- coding: utf-8 -*-
"""Exam Cheatsheet & Master Reference Module"""

def get_exam_cheatsheet_content():
    return """
        <!-- ============================================================ -->
        <!-- MASTER EXAM DAY CHEATSHEET & SUGGESTER -->
        <!-- ============================================================ -->
        <article class="master-cheatsheet" id="master-exam-cheatsheet">
            <header style="border-bottom: 3px solid var(--accent-gold); padding-bottom: 16px; margin-bottom: 24px;">
                <h2 style="font-size: 1.6rem; color: var(--primary-navy); display: flex; align-items: center; gap: 10px;">
                    <span>🎓</span>
                    <span>Master Exam Day Cheatsheet &amp; Strategy Suggester</span>
                </h2>
                <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 4px;">
                    Curated high-yield formula index, cross-module R command dictionary, and the top 10 lethal NPTEL exam traps.
                </p>
            </header>

            <!-- Top 25 High-Yield Formulas -->
            <section style="margin-bottom: 34px;">
                <h3 style="font-size: 1.15rem; color: var(--secondary-navy); margin-bottom: 14px; font-weight: 700;">
                    ⭐ Top 25 High-Yield Exam Formulas Quick-Index
                </h3>
                <div class="table-responsive">
                    <table class="academic-table">
                        <thead>
                            <tr>
                                <th>Week &amp; Domain</th>
                                <th>Concept / Target</th>
                                <th>Formula / Condition</th>
                                <th>Key Exam Insight</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>W1: R Basics</strong></td>
                                <td>Matrix Multiplication</td>
                                <td>$A_{(m \\times k)} \\mathbin{\\%*\\%} B_{(k \\times n)} = C_{(m \\times n)}$</td>
                                <td>Inner dimensions must match; standard <code>*</code> is element-wise!</td>
                            </tr>
                            <tr>
                                <td><strong>W2: Lin Alg</strong></td>
                                <td>2x2 Eigenvalue Shortcut</td>
                                <td>$\\lambda^2 - \\text{tr}(A)\\lambda + \\det(A) = 0$</td>
                                <td>Trace = sum of eigenvalues; Det = product of eigenvalues.</td>
                            </tr>
                            <tr>
                                <td><strong>W2: Lin Alg</strong></td>
                                <td>Polynomial Det Shift</td>
                                <td>$\\det(A - cI) = \\prod_{i=1}^n (\\lambda_i - c)$</td>
                                <td>Never reconstruct matrix; subtract $c$ from each eigenvalue and multiply.</td>
                            </tr>
                            <tr>
                                <td><strong>W2: Lin Alg</strong></td>
                                <td>Orthogonality</td>
                                <td>$u^T v = \\sum u_i v_i = 0$</td>
                                <td>Two vectors are perpendicular iff dot product is 0.</td>
                            </tr>
                            <tr>
                                <td><strong>W2: Lin Alg</strong></td>
                                <td>Linear Consistency</td>
                                <td>$\\text{rank}(A) = \\text{rank}([A \\mid b])$</td>
                                <td>Unique if rank $= n$; infinite if rank $&lt; n$; none if rank(A) &lt; rank([A|b]).</td>
                            </tr>
                            <tr>
                                <td><strong>W3: Stats</strong></td>
                                <td>Variance of Linear Comb</td>
                                <td>$\\text{Var}(aX - bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y)$</td>
                                <td>Independent vars: notice the PLUS sign between terms!</td>
                            </tr>
                            <tr>
                                <td><strong>W3: Stats</strong></td>
                                <td>One-Sample Z-Test</td>
                                <td>$Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}}$</td>
                                <td>Reject $H_0$ if $|Z| &gt; 1.96$ at $\\alpha = 0.05$ (two-tailed) or $p &lt; \\alpha$.</td>
                            </tr>
                            <tr>
                                <td><strong>W3: Stats</strong></td>
                                <td>Sample Variance</td>
                                <td>$s^2 = \\frac{1}{n-1}\\sum (X_i - \\bar{X})^2$</td>
                                <td>Divisor is $n-1$ (Bessel's correction) to ensure unbiasedness.</td>
                            </tr>
                            <tr>
                                <td><strong>W4: Univar Opt</strong></td>
                                <td>FONC &amp; SOSC</td>
                                <td>$f'(x^*) = 0$; $f'' &gt; 0 \\implies \\min$; $f'' &lt; 0 \\implies \\max$</td>
                                <td>If $f'' = 0$ and $f''' \\ne 0 \\implies$ inflection point!</td>
                            </tr>
                            <tr>
                                <td><strong>W4: Univar Opt</strong></td>
                                <td>Newton-Raphson Opt</td>
                                <td>$x_{k+1} = x_k - \\frac{f'(x_k)}{f''(x_k)}$</td>
                                <td>Uses ratio of 1st derivative over 2nd derivative.</td>
                            </tr>
                            <tr>
                                <td><strong>W5: Multivar Opt</strong></td>
                                <td>Hessian Definiteness</td>
                                <td>$\\lambda_i(H) &gt; 0 \\; \\forall i \\implies \\min$; $\\lambda_i &lt; 0 \\implies \\max$</td>
                                <td>Mixed eigenvalue signs $\implies$ Saddle point. Hessian is always symmetric!</td>
                            </tr>
                            <tr>
                                <td><strong>W5: Multivar Opt</strong></td>
                                <td>Lagrange Multipliers</td>
                                <td>$\\nabla f(x) + \\lambda \\nabla g(x) = 0, \\quad g(x) = 0$</td>
                                <td>Gradient of objective is collinear with gradient of constraint.</td>
                            </tr>
                            <tr>
                                <td><strong>W6: Regression</strong></td>
                                <td>OLS Slope &amp; Intercept</td>
                                <td>$\\hat{\\beta}_1 = \\frac{\\text{Cov}(X,Y)}{\\text{Var}(X)} = r\\frac{s_Y}{s_X}, \\quad \\hat{\\beta}_0 = \\bar{Y} - \\hat{\\beta}_1 \\bar{X}$</td>
                                <td>Regression line always passes through centroid $(\\bar{X}, \\bar{Y})$.</td>
                            </tr>
                            <tr>
                                <td><strong>W6: Regression</strong></td>
                                <td>Residual Error</td>
                                <td>$e_i = Y_i - \\hat{Y}_i$</td>
                                <td>Always Actual minus Predicted! Positive $e \\implies$ underpredicted.</td>
                            </tr>
                            <tr>
                                <td><strong>W6: Regression</strong></td>
                                <td>ANOVA Identity</td>
                                <td>$\\text{SST} = \\text{SSR} + \\text{SSE}$</td>
                                <td>$R^2 = \\text{SSR}/\\text{SST} = 1 - \\text{SSE}/\\text{SST}$. Total variance = regression + error.</td>
                            </tr>
                            <tr>
                                <td><strong>W6: Regression</strong></td>
                                <td>Adjusted $R^2$</td>
                                <td>$\\text{Adj } R^2 = 1 - (1 - R^2)\\frac{n-1}{n-p-1} = 1 - \\frac{\\text{SSE}/(n-p-1)}{\\text{SST}/(n-1)}$</td>
                                <td>Penalizes adding non-informative variables.</td>
                            </tr>
                            <tr>
                                <td><strong>W7: Logistic Reg</strong></td>
                                <td>Sigmoid Function</td>
                                <td>$p(X) = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 X)}}$</td>
                                <td>Maps linear scale into $(0, 1)$ probability.</td>
                            </tr>
                            <tr>
                                <td><strong>W7: Logistic Reg</strong></td>
                                <td>Odds &amp; Logit</td>
                                <td>$\\text{Odds} = \\frac{p}{1-p} = e^{\\beta_0 + \\beta_1 X}, \\quad \\text{logit}(p) = \\beta_0 + \\beta_1 X$</td>
                                <td>1-unit increase in $X$ multiplies odds by $e^{\\beta_1}$.</td>
                            </tr>
                            <tr>
                                <td><strong>W7: Classification</strong></td>
                                <td>Sensitivity (Recall)</td>
                                <td>$\\text{Sensitivity} = \\frac{TP}{TP + FN}$</td>
                                <td>Denominator is Actual Positives. False Negatives are zero if 100%.</td>
                            </tr>
                            <tr>
                                <td><strong>W7: Classification</strong></td>
                                <td>Specificity</td>
                                <td>$\\text{Specificity} = \\frac{TN}{TN + FP}$</td>
                                <td>Denominator is Actual Negatives. FPR $= 1 - \\text{Specificity}$.</td>
                            </tr>
                            <tr>
                                <td><strong>W7: Classification</strong></td>
                                <td>Precision</td>
                                <td>$\\text{Precision} = \\frac{TP}{TP + FP}$</td>
                                <td>Denominator is Predicted Positives.</td>
                            </tr>
                            <tr>
                                <td><strong>W1: R Basics</strong></td>
                                <td>String Concatenation</td>
                                <td><code>paste(..., sep)</code> vs <code>paste(..., collapse)</code></td>
                                <td><code>sep</code> joins parallel elements; <code>collapse</code> squashes vector into 1 scalar string.</td>
                            </tr>
                            <tr>
                                <td><strong>W2: Lin Alg</strong></td>
                                <td>Rank-1 Outer Product</td>
                                <td>$\\lambda_1 = \\|u\\|_2^2 = \\text{tr}(u u^T), \\quad \\lambda_{2..n} = 0$</td>
                                <td>Outer product has rank 1. All other eigenvalues are 0. Sum of pairwise products is 0.</td>
                            </tr>
                            <tr>
                                <td><strong>W3: Stats</strong></td>
                                <td>Categorical Central Tendency</td>
                                <td>$\\text{Mode}$ is the ONLY valid metric for nominal data</td>
                                <td>You cannot compute mean or median of qualitative labels (e.g. eye color, machine brand).</td>
                            </tr>
                            <tr>
                                <td><strong>W3: Stats</strong></td>
                                <td>Sample Variance Distribution</td>
                                <td>$\\frac{(n - 1)s^2}{\\sigma^2} \\sim \\chi^2_{n - 1}$</td>
                                <td>Scaled sample variance follows Chi-Square with $n-1$ df; expected value is $n-1$.</td>
                            </tr>
                            <tr>
                                <td><strong>W5: Multivar Opt</strong></td>
                                <td>2D Sylvester's Criterion</td>
                                <td>$ac - b^2 &gt; 0, a &gt; 0 \\implies \\min; \\quad ac - b^2 &lt; 0 \\implies \\text{saddle}$</td>
                                <td>Direct determinant test for $2 \\times 2$ Hessian $H = \\begin{bmatrix} a &amp; b \\\\ b &amp; c \\end{bmatrix}$.</td>
                            </tr>
                            <tr>
                                <td><strong>W6: Regression</strong></td>
                                <td>Confidence vs Prediction Int</td>
                                <td>$\\text{SE}(Y_{\\text{new}}) = s_e\\sqrt{1 + \\frac{1}{n} + \\frac{(X_0-\\bar{X})^2}{S_{XX}}}$</td>
                                <td>Prediction Interval for individual is ALWAYS strictly wider than Confidence Interval for mean!</td>
                            </tr>
                            <tr>
                                <td><strong>W8: KNN</strong></td>
                                <td>Bias-Variance vs $K$</td>
                                <td>Small $K \\implies$ High Var, Low Bias; Large $K \\implies$ Low Var, High Bias</td>
                                <td>KNN works for both binary and multiclass classification &amp; regression!</td>
                            </tr>
                            <tr>
                                <td><strong>W8: Clustering</strong></td>
                                <td>Clustering Conservation</td>
                                <td>$\\text{TSS} = \\text{BCSS} + \\text{WSS}$</td>
                                <td>$\\text{BCSS} = \\text{TSS} - \\text{WSS}$. Maximizing BCSS/TSS improves quality.</td>
                            </tr>
                            <tr>
                                <td><strong>W8: Clustering</strong></td>
                                <td>Scaled Total SS Shortcut</td>
                                <td>$\\text{TSS}_{\\text{scaled}} = (n - 1) \\times p$</td>
                                <td>For $n=50$ states and $p=4$ variables: $\\text{TSS} = 49 \\times 4 = 196$.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- The 12 Most Lethal Exam Traps -->
            <section style="margin-bottom: 34px;">
                <h3 style="font-size: 1.15rem; color: var(--danger-red); margin-bottom: 14px; font-weight: 700;">
                    ⚠️ The 12 Most Lethal NPTEL Exam Traps &amp; How to Evade Them
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 14px;">
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">1</div>
                        <div class="callout-content">
                            <h4>ls() vs dir()</h4>
                            <p><code class="inline-code">ls()</code> displays objects in the active R session RAM. It does NOT list files on disk! Use <code class="inline-code">list.files()</code> or <code class="inline-code">dir()</code> for disk files.</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">2</div>
                        <div class="callout-content">
                            <h4>Negative Slicing A[-2, ]</h4>
                            <p>In R, negative indices mean <strong>drop/exclude</strong>! <code class="inline-code">A[-2, ]</code> deletes row 2; it does NOT select the 2nd row from the bottom.</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">3</div>
                        <div class="callout-content">
                            <h4>Variance of Difference</h4>
                            <p>For independent variables: $\\text{Var}(aX - bY) = a^2\\text{Var}(X) \\mathbf{+} b^2\\text{Var}(Y)$. The minus sign squares to positive! Variances always add.</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">4</div>
                        <div class="callout-content">
                            <h4>Gradient vs Contours</h4>
                            <p>The gradient $\\nabla f$ is strictly <strong>orthogonal / perpendicular</strong> to contour lines, NEVER parallel!</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">5</div>
                        <div class="callout-content">
                            <h4>Hessian Symmetry</h4>
                            <p>By Schwarz's theorem, mixed partials commute ($\\frac{\\partial^2 f}{\\partial x_i \\partial x_j} = \\frac{\\partial^2 f}{\\partial x_j \\partial x_i}$). Hence Hessian $H$ is ALWAYS symmetric ($H = H^T$).</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">6</div>
                        <div class="callout-content">
                            <h4>Residual Error Sign</h4>
                            <p>Residual error is defined as $e = Y_{\\text{actual}} - \\hat{Y}_{\\text{predicted}}$. Never compute Predicted minus Actual!</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">7</div>
                        <div class="callout-content">
                            <h4>Bias-Variance is NOT a CV Technique</h4>
                            <p>LOOCV, $k$-fold, and validation sets are cross-validation methods. Bias-variance trade-off is an algorithm property, not a validation technique!</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">8</div>
                        <div class="callout-content">
                            <h4>glm() Requires family = binomial</h4>
                            <p>Fitting logistic regression requires <code class="inline-code">family = binomial</code>. Without it, R fits ordinary linear regression!</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">9</div>
                        <div class="callout-content">
                            <h4>predict() type = "response"</h4>
                            <p>To obtain probabilities $p \\in [0, 1]$, you MUST pass <code class="inline-code">type = "response"</code>. Default output is the unconstrained logit $\\beta_0 + \\beta_1 X$.</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">10</div>
                        <div class="callout-content">
                            <h4>KNN is NOT Binary-Only</h4>
                            <p>KNN works effortlessly for multi-class classification and continuous regression problems!</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">11</div>
                        <div class="callout-content">
                            <h4>Central Tendency for Categorical Data</h4>
                            <p>Mode is the <strong>ONLY</strong> central tendency measure applicable to nominal / categorical data. Mean and median are mathematically undefined for qualitative categories.</p>
                        </div>
                    </div>
                    <div class="callout-card callout-trap" style="margin: 0;">
                        <div class="callout-icon">12</div>
                        <div class="callout-content">
                            <h4>Prediction vs Confidence Interval</h4>
                            <p>A Prediction Interval for a single new observation $Y_{\\text{new}}$ is <strong>ALWAYS strictly wider</strong> than the Confidence Interval for the mean response $E[Y|X_0]$ due to the extra individual variance $+1$.</p>
                        </div>
                    </div>
                </div>
            </section>
        </article>

        <!-- Footer -->
        <footer style="margin-top: 50px; padding: 28px 0; border-top: 2px solid var(--border-light); text-align: center; color: var(--text-muted); font-size: 0.85rem;">
            <p style="font-weight: 600; color: var(--primary-navy); margin-bottom: 4px;">
                NPTEL Data Science for Engineers — Comprehensive Master Study Guide (Weeks 1 to 8)
            </p>
            <p>
                Synthesized from official IIT Madras lecture notes and graded assignments. Compiled for high-performance exam revision.
            </p>
            <div style="margin-top: 10px;">
                <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" style="background: var(--primary-navy); color: white; border: none; padding: 6px 14px; border-radius: 4px; font-size: 0.78rem; cursor: pointer; font-weight: 600;">
                    ▲ Back to Top
                </button>
            </div>
        </footer>
    </main>
</div>

<!-- Interactive Client-side Scripts -->
<script>
    // Live Search Filter for Navigation and Topics
    function filterNav() {
        const query = document.getElementById('navSearch').value.toLowerCase();
        const navItems = document.querySelectorAll('#navList .nav-item');
        
        navItems.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(query)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    }

    // Toggle All Solutions for Self-Testing
    let solutionsExpanded = false;
    function toggleAllSolutions() {
        const drawers = document.querySelectorAll('details.solution-drawer');
        solutionsExpanded = !solutionsExpanded;
        drawers.forEach(d => {
            d.open = solutionsExpanded;
        });
        const btn = document.getElementById('btn-toggle-solutions');
        btn.textContent = solutionsExpanded ? '🙈 Collapse Solutions' : '👁️ Toggle Solutions';
    }

    // Smooth Scroll for Internal Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetEl = document.getElementById(targetId);
            if (targetEl) {
                targetEl.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
</script>

</body>
</html>
"""

print("Cheatsheet and footer loaded.")
