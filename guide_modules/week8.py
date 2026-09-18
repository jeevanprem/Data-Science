# -*- coding: utf-8 -*-
"""Week 8 Module: Supervised (KNN) & Unsupervised Learning (K-Means Clustering)"""

def get_week8_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 8 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week8">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 08</span> KNN &amp; K-Means Clustering</h2>
                    <div class="module-lectures">NPTEL Lectures 46–50 | Supervised vs Unsupervised, K-Nearest Neighbors, K-Means Clustering, and USArrests Case Study</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        The final module synthesizes machine learning paradigms by contrasting supervised instance-based learning ($K$-Nearest Neighbors) with unsupervised clustering ($K$-Means). Both algorithms rely fundamentally on geometric distance metrics in multidimensional feature space.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Supervised vs Unsupervised Learning Paradigms</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Supervised Learning:</strong> Every training instance possesses an input feature vector $X_i$ paired with an explicit ground-truth supervisor label $Y_i$. Objective: learn mapping $f: X \\to Y$.
                                <br>• Continuous $Y \\implies$ <strong>Regression</strong> (Linear Regression, KNN Regressor).
                                <br>• Categorical $Y \\implies$ <strong>Classification</strong> (Logistic Regression, KNN Classifier).
                            </li>
                            <li><strong>Unsupervised Learning:</strong> Data consists solely of input features $X_i$ with <em>no target labels</em> $Y$. Objective: discover latent groupings, natural cluster boundaries, or compact manifold representations ($K$-Means, Hierarchical Clustering, PCA).
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. K-Nearest Neighbors (KNN) Algorithm</h4>
                        <p>
                            KNN is a non-parametric, memory-based "lazy learner" that does not construct an explicit mathematical model during training. It simply memorizes the training data:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Algorithm Procedure:</strong> For an unlabelled query point $x_0$:
                                <br>1. Calculate distance from $x_0$ to all $n$ training instances using an appropriate metric:
                                <br>• <em>Euclidean Distance ($L_2$):</em> $d(x_0, x_i) = \\sqrt{\\sum_{j=1}^p (x_{0,j} - x_{i,j})^2}$
                                <br>• <em>Manhattan Distance ($L_1$):</em> $d(x_0, x_i) = \\sum_{j=1}^p |x_{0,j} - x_{i,j}|$
                                <br>• <em>Chebyshev Distance ($L_\\infty$):</em> $d(x_0, x_i) = \\max_{1 \\le j \\le p} |x_{0,j} - x_{i,j}|$
                                <br>• <em>Minkowski Distance ($L_q$):</em> $d(x_0, x_i) = \\left(\\sum_{j=1}^p |x_{0,j} - x_{i,j}|^q\\right)^{1/q}$
                                <br>2. Identify the set $\\mathcal{N}_K(x_0)$ of the $K$ closest training points.
                                <br>3. <strong>Classification:</strong> Assign $x_0$ to the majority class via voting: $\\hat{Y} = \\operatorname{mode}(\\{y_i \\mid i \\in \\mathcal{N}_K\\})$.
                                <br>4. <strong>Regression:</strong> Predict the average response: $\\hat{Y} = \\frac{1}{K}\\sum_{i \\in \\mathcal{N}_K} y_i$ (or distance-weighted average).
                            </li>
                            <li><strong>Choice of Hyperparameter $K$ &amp; Bias–Variance Tradeoff:</strong>
                                <br>• <em>Odd $K$:</em> Choosing an odd $K$ (e.g. $3, 5, 7$) is standard for binary classification to unconditionally prevent ties in majority voting.
                                <br>• <em>Small $K$ ($K = 1$):</em> Highly flexible boundary, zero training error, sensitive to noise/outliers $\\implies$ <strong>High Variance, Low Bias</strong> (Overfitting).
                                <br>• <em>Large $K$ ($K \\to n$):</em> Rigid, smooth boundary, highly stable against noise, but predicts global training class proportion $\\implies$ <strong>Low Variance, High Bias</strong> (Underfitting).
                                <br>• <em>Tuning:</em> Optimal $K$ is selected via cross-validation.
                            </li>
                            <li><strong>Essential Properties of KNN:</strong>
                                <br>• KNN works for <strong>BOTH binary AND multi-class classification</strong> as well as continuous regression!
                                <br>• <strong>Feature Scaling is Mandatory:</strong> Unscaled variables with large ranges overwhelm distance metrics. Always preprocess features with <code class="inline-code">scale()</code>.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. K-Means Clustering: Lloyd's Algorithm &amp; Objective Function</h4>
                        <p>
                            $K$-Means partitions $n$ observations into $K$ non-overlapping clusters $C_1, C_2, \\dots, C_K$ such that each observation belongs to the cluster with the nearest centroid.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Mathematical Objective:</strong> Minimize the total <strong>Within-Cluster Sum of Squares (WSS)</strong>:
                                $$\\min_{C_1, \\dots, C_K} \\sum_{k=1}^K \\text{WSS}_k = \\sum_{k=1}^K \\sum_{x_i \\in C_k} \\|x_i - \\mu_k\\|^2$$
                                where $\\mu_k = \\frac{1}{|C_k|}\\sum_{x_i \\in C_k} x_i$ is the mean vector (centroid) of cluster $C_k$.
                            </li>
                            <li><strong>Lloyd's Iterative Protocol:</strong>
                                <br>1. Choose number of clusters $K$.
                                <br>2. Randomly initialize $K$ cluster centroids $\\mu_1, \\dots, \\mu_K$.
                                <br>3. <strong>Assignment Step:</strong> Assign each data point to its nearest centroid based on Euclidean distance:
                                $$c_i = \\arg\\min_{1 \\le k \\le K} \\|x_i - \\mu_k\\|^2$$
                                <br>4. <strong>Update Step:</strong> Recompute each centroid as the arithmetic mean of all assigned points:
                                $$\\mu_k = \\frac{1}{|C_k|}\\sum_{x_i \\in C_k} x_i$$
                                <br>5. Repeat steps 3 and 4 until cluster assignments stabilize (convergence).
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Sum of Squares Decomposition in K-Means</h4>
                        <p>
                            Similar to regression ANOVA, the dispersion in clustering decomposes into:
                            $$\\mathbf{\\text{Total Sum of Squares (TSS)} = \\text{Between-Cluster SS (BCSS)} + \\text{Within-Cluster SS (WSS)}}$$
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Total Sum of Squares (TSS):</strong> Total dispersion of all $n$ points around the global grand mean $\\bar{x}$:
                                $$\\text{TSS} = \\sum_{i=1}^n \\|x_i - \\bar{x}\\|^2$$
                                <strong>Professor's Scaled TSS Shortcut:</strong> If features are normalized using <code class="inline-code">scale()</code>, each feature has sample variance $= 1$. For $n$ observations and $p$ features:
                                $$\\mathbf{\\text{TSS} = (n - 1) \\times p}$$
                                For the standard <code class="inline-code">USArrests</code> dataset ($n = 50, p = 4$), $\\text{TSS} = (50 - 1) \\times 4 = \\mathbf{196}$!
                            </li>
                            <li><strong>Within-Cluster Sum of Squares (WSS):</strong> Compactness of clusters:
                                $$\\text{WSS} = \\sum_{k=1}^K \\sum_{x_i \\in C_k} \\|x_i - \\mu_k\\|^2$$
                            </li>
                            <li><strong>Between-Cluster Sum of Squares (BCSS):</strong> Separation between cluster centroids:
                                $$\\text{BCSS} = \\sum_{k=1}^K |C_k| \\|\\mu_k - \\bar{x}\\|^2 = \\text{TSS} - \\text{WSS}$$
                            </li>
                            <li>A superior clustering solution maximizes the ratio $\\frac{\\text{BCSS}}{\\text{TSS}} \\to 100\\%$.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Selecting Optimal $K$ &amp; Local Minima</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Elbow Method (Scree Plot):</strong> Plot total WSS against $K$. The curve drops rapidly initially and then flattens. The "elbow" indicates the point of diminishing returns, representing the optimal $K$.</li>
                            <li><strong>Dendrogram:</strong> Tree diagram produced by Hierarchical Clustering to determine cluster count by cutting branches.</li>
                            <li><strong>Why Scatter Plot is NOT Useful:</strong> A 2D scatter plot cannot handle multidimensional data ($p &gt; 2$), nor does it provide a mathematical variance criterion to select $K$.</li>
                            <li><strong>Sensitivity to Initial Centroids &amp; nstart:</strong> $K$-Means converges to a <em>local minimum</em>. To find the true optimal partition, R provides the <code class="inline-code">nstart</code> parameter (e.g. <code class="inline-code">nstart = 20</code>), which runs 20 separate random initializations and retains the model with the minimum total WSS.</li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Scaled TSS &amp; KNN Capabilities</h4>
                            <p>
                                <strong>Trap 1:</strong> <em>"KNN works ONLY for binary classification."</em> $\\implies$ <strong>FALSE!</strong> KNN readily handles multiclass targets ($C &gt; 2$) and regression problems.
                                <br><strong>Trap 2:</strong> <em>"Which method is NOT useful to determine the optimal number of clusters?"</em> $\\implies$ <strong>Scatter plot</strong>. (Elbow method and Dendrogram are valid).
                                <br><strong>Trap 3:</strong> In the <code class="inline-code">USArrests</code> problem, students often waste 10 minutes calculating TSS. On scaled data with $n=50, p=4$, $\\text{TSS} = 49 \\times 4 = 196$. It falls strictly in the range <strong>100–200</strong>!
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's K-Means Identity Blueprint</h4>
                            <p>
                                Always remember the clustering conservation law:
                                $$\\text{TSS} = \\text{BCSS} + \\text{WSS}$$
                                If the question asks for BCSS:
                                <br>1. Calculate or extract $\\text{WSS} = \\sum_{k=1}^K \\text{withinss}_k$.
                                <br>2. Obtain $\\text{TSS} = (n-1)p$.
                                <br>3. Compute $\\text{BCSS} = \\text{TSS} - \\text{WSS}$ immediately.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Essential Mathematical Formulas &amp; Clustering Metrics</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>K-Means Objective (WSS)</span>
                                <span class="nav-badge">Compactness</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{WSS} = \\sum_{k=1}^K \\sum_{x_i \\in C_k} \\|x_i - \\mu_k\\|^2$$
                            </div>
                            <div class="formula-desc">Sum of squared Euclidean distances of each point from its assigned cluster centroid. Lloyd's algorithm minimizes this function.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Points $(1, 2)$ and $(3, 4)$ form cluster $k$. Find centroid $\\mu_k$ and $\\text{WSS}_k$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Centroid $\\mu_k = (2, 3)$. Squared distances: $\\|(1,2)-(2,3)\\|^2 = 1+1 = 2$; $\\|(3,4)-(2,3)\\|^2 = 1+1 = 2$. Thus $\\text{WSS}_k = 2 + 2 = 4$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is $\\text{WSS}$ when $K = n$ (number of clusters equals sample size)?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Every point is its own centroid ($x_i = \\mu_i$), so $\\text{WSS} = 0$. The elbow method selects the point where marginal reduction in $\\text{WSS}$ drops off sharply.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Clustering Conservation Law</span>
                                <span class="nav-badge">Decomposition</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{TSS} = \\text{BCSS} + \\text{WSS}$$
                            </div>
                            <div class="formula-desc">Total sum of squares equals between-cluster dispersion plus within-cluster dispersion.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If a 3-cluster clustering yields $\\text{TSS} = 200$ and total $\\text{WSS} = 50$, compute $\\text{BCSS}$ and explained variance ratio.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{BCSS} = \\text{TSS} - \\text{WSS} = 200 - 50 = 150$. Ratio $\\frac{\\text{BCSS}}{\\text{TSS}} = \\frac{150}{200} = 0.75$ (75% of total variance explained by cluster separation).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> In R's <code>kmeans()</code>, how is clustering quality evaluated?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Higher ratio <code>betweenss / totss</code> closer to $100\\%$ indicates well-separated, compact clusters.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Scaled TSS Formula</span>
                                <span class="nav-badge">Standardization</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{TSS}_{\\text{scaled}} = (n - 1) \\times p$$
                            </div>
                            <div class="formula-desc">For standardized data ($z$-scores), each feature has unit variance $s^2 = 1$. Total SS is exactly $(n-1)p$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Standardized dataset <code>USArrests</code> has $n = 50$ states and $p = 4$ variables. Find $\\text{TSS}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{TSS} = (n - 1) \\times p = (50 - 1) \\times 4 = 49 \\times 4 = 196$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Why is standardization via <code>scale()</code> essential before K-means?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Prevents variables with arbitrarily large numerical scales (e.g., income in thousands vs. age in years) from dominating Euclidean distance calculations.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Euclidean Distance ($L_2$)</span>
                                <span class="nav-badge">Distance</span>
                            </div>
                            <div class="formula-math">
                                $$d(x_i, x_j) = \\sqrt{\\sum_{r=1}^p (x_{ir} - x_{jr})^2}$$
                            </div>
                            <div class="formula-desc">Standard distance metric governing cluster assignment in K-means and neighborhood voting in KNN.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Find distance between query $q = (2, 3)$ and points $a = (5, 7)$ and $b = (1, 1)$. Which is closer?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $d(q, a) = \\sqrt{(2-5)^2 + (3-7)^2} = \\sqrt{9+16} = 5.0$. $d(q, b) = \\sqrt{(2-1)^2 + (3-1)^2} = \\sqrt{1+4} = \\sqrt{5} \\approx 2.236$. Point $b$ is the 1-NN.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $K=3$ nearest neighbors have class labels $\\{A, B, A\\}$, what does KNN predict?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Majority vote gives Class $A$ with posterior probability $P(Y=A \\mid x) = 2/3 \\approx 66.7\\%$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Manhattan ($L_1$) &amp; Chebyshev ($L_\\infty$)</span>
                                <span class="nav-badge">Distance Metrics</span>
                            </div>
                            <div class="formula-math">
                                $$d_1(u, v) = \\sum_{r=1}^p |u_r - v_r|, \\quad d_\\infty(u, v) = \\max_{1 \\le r \\le p} |u_r - v_r|$$
                            </div>
                            <div class="formula-desc">Alternative geometric distances. For all vector pairs in $\\mathbb{R}^p$, the strict norm ordering $d_\\infty \\le d_2 \\le d_1$ holds.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Compute $L_1$ and $L_\\infty$ distances between $u = (1, 4)$ and $v = (5, 1)$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Absolute differences are $|1-5| = 4$ and $|4-1| = 3$. Manhattan $d_1 = 4 + 3 = 7.0$. Chebyshev $d_\\infty = \\max(4, 3) = 4.0$. (Euclidean is $5.0$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> How do $L_1, L_2, L_\\infty$ compare in magnitude?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Always $d_\\infty(u, v) \\le d_2(u, v) \\le d_1(u, v)$. In the example: $4.0 \\le 5.0 \\le 7.0$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Between-Cluster SS (BCSS)</span>
                                <span class="nav-badge">Separation</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{BCSS} = \\sum_{k=1}^K |C_k| \\|\\mu_k - \\bar{x}\\|^2 = \\text{TSS} - \\text{WSS}$$
                            </div>
                            <div class="formula-desc">Measures between-cluster separation (dispersion of cluster centroids around global grand mean). Maximizing BCSS/TSS yields optimal clusters.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> $10$ points partition into 2 clusters around grand mean $\\bar{x} = 0$: $n_1 = 6, \\mu_1 = 2$; $n_2 = 4, \\mu_2 = -3$. Compute $\\text{BCSS}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{BCSS} = 6(2 - 0)^2 + 4(-3 - 0)^2 = 6(4) + 4(9) = 24 + 36 = 60.0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $\\text{TSS} = 100$ and $\\text{BCSS} = 60$, calculate $\\text{WSS}$ and variance explained.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{WSS} = \\text{TSS} - \\text{BCSS} = 100 - 60 = 40.0$. Variance explained ratio is $\\frac{\\text{BCSS}}{\\text{TSS}} = \\frac{60}{100} = 60.0\\%$.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Clustering &amp; KNN Functions</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Property</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Description &amp; Operation</th>
                                    <th>Practical Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">scale()</span></td>
                                    <td><code class="inline-code">scale(x, center = TRUE, scale = TRUE)</code></td>
                                    <td>Centers and scales columns of numeric matrix to mean 0, variance 1.</td>
                                    <td><code class="inline-code">scaled_data &lt;- scale(USArrests)</code></td>
                                    <td>Standardized matrix of $z$-scores</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">kmeans()</span></td>
                                    <td><code class="inline-code">kmeans(x, centers, nstart = 1)</code></td>
                                    <td>Executes $K$-means clustering. <code class="inline-code">nstart &gt; 1</code> tests multiple initial starts.</td>
                                    <td><code class="inline-code">km &lt;- kmeans(scaled_data, centers=4, nstart=20)</code></td>
                                    <td>Fitted <code class="inline-code">kmeans</code> clustering object</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">$withinss</span></td>
                                    <td><code class="inline-code">km$withinss</code></td>
                                    <td>Vector of within-cluster sum of squares, one entry per cluster.</td>
                                    <td><code class="inline-code">km$withinss</code></td>
                                    <td><code class="inline-code">c(8.32, 11.95, 16.21, 19.92)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">$size</span></td>
                                    <td><code class="inline-code">km$size</code></td>
                                    <td>Number of observations allocated to each cluster.</td>
                                    <td><code class="inline-code">km$size</code></td>
                                    <td><code class="inline-code">c(8, 13, 16, 13)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">$betweenss</span></td>
                                    <td><code class="inline-code">km$betweenss</code></td>
                                    <td>Between-cluster sum of squares (separation between centroids).</td>
                                    <td><code class="inline-code">km$betweenss</code></td>
                                    <td><code class="inline-code">139.597</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">$totss</span></td>
                                    <td><code class="inline-code">km$totss</code></td>
                                    <td>Total sum of squares across all data points ($196$ for USArrests).</td>
                                    <td><code class="inline-code">km$totss</code></td>
                                    <td><code class="inline-code">196</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">class::knn()</span></td>
                                    <td><code class="inline-code">knn(train, test, cl, k = 1)</code></td>
                                    <td>$K$-Nearest Neighbor classification. <code class="inline-code">cl</code> is factor of true class labels.</td>
                                    <td><code class="inline-code">knn(train_x, test_x, train_y, k=3)</code></td>
                                    <td>Factor vector of predicted classes</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">dist()</span></td>
                                    <td><code class="inline-code">dist(x, method = "euclidean")</code></td>
                                    <td>Computes distance matrix using <code class="inline-code">"euclidean"</code>, <code class="inline-code">"manhattan"</code>, or <code class="inline-code">"maximum"</code>.</td>
                                    <td><code class="inline-code">dist(df, method = "manhattan")</code></td>
                                    <td>Pairwise distance matrix object</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">hclust() / cutree()</span></td>
                                    <td><code class="inline-code">hclust(d, method = "complete")</code></td>
                                    <td>Hierarchical agglomerative clustering on distance matrix; <code class="inline-code">cutree(hc, k=3)</code> extracts cluster vector.</td>
                                    <td><code class="inline-code">hc &lt;- hclust(dist(df)); cutree(hc, 3)</code></td>
                                    <td>Cluster tree dendrogram / cluster label vector</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block" id="week8-practice">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Clustering Basis in K-Means</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> The $K$-means clustering algorithm clusters the data points based on:</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> Dependent and independent variables</li>
                                <li><span class="opt-bullet">B.</span> The eigenvalues of the covariance matrix</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> Distance between the points and a cluster centre</li>
                                <li><span class="opt-bullet">D.</span> Maximum margin hyperplane separation</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Algorithmic Mechanics</div>
                                    <p>
                                        $K$-means is an unsupervised algorithm (hence no dependent variables exist). In the assignment step, every data point $x_i$ is assigned to cluster $C_k$ whose centroid $\\mu_k$ minimizes Euclidean distance:
                                        $$c_i = \\arg\\min_k \\|x_i - \\mu_k\\|^2$$
                                        Therefore, clustering is performed strictly based on the <strong>distance between the data points and the cluster centre</strong>.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option C (Distance between the points and a cluster centre)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Metrics for Choosing Number of Clusters</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> The method / metric which is <strong>NOT USEFUL</strong> to determine the optimal number of clusters in unsupervised clustering algorithms is:</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> Scatter plot</li>
                                <li><span class="opt-bullet">B.</span> Elbow method</li>
                                <li><span class="opt-bullet">C.</span> Dendrogram</li>
                                <li><span class="opt-bullet">D.</span> Silhouette coefficient</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Methodology Comparison</div>
                                    <p>
                                        • <strong>Elbow method:</strong> Evaluates total WSS reduction as a function of $K$.
                                        <br>• <strong>Dendrogram:</strong> Tree diagram in hierarchical clustering explicitly designed to choose cluster count by height cutoff.
                                        <br>• <strong>Silhouette coefficient:</strong> Quantifies cluster separation vs cohesion across varying $K$.
                                        <br>• <strong>Scatter plot:</strong> Only visualizes 2 dimensions at a time, cannot evaluate multidimensional data, and provides no mathematical metric to objectively determine $K$.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (Scatter plot)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Properties of K-Nearest Neighbors</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> Which of the following statements is <strong>INCORRECT</strong> about the KNN algorithm?</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> KNN works ONLY for binary classification problems.</li>
                                <li><span class="opt-bullet">B.</span> If $k = 1$, then the algorithm is simply called the nearest neighbor algorithm.</li>
                                <li><span class="opt-bullet">C.</span> The number of neighbours ($K$) will influence classification output.</li>
                                <li><span class="opt-bullet">D.</span> KNN is a non-parametric instance-based algorithm.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Analysis of KNN Statements</div>
                                    <p>
                                        • Statement A asserts KNN works <em>only</em> for binary problems. This is <strong>INCORRECT</strong>. KNN naturally extends to multi-class classification ($C &gt; 2$) by taking the plurality class among $K$ neighbors, and to regression by averaging neighbor responses!
                                        <br>• Statements B, C, and D are factually correct statements.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (KNN works ONLY for binary classification is INCORRECT)
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase filter-item filter-assignment">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 8 Comprehensive | USArrests Case Study</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: Standardized K-Means Clustering on USArrests Dataset
                            </p>
                            <p>
                                Consider the classic benchmark dataset <code class="inline-code">USArrests</code> containing statistics in arrests per 100,000 residents for <strong>Murder</strong>, <strong>Assault</strong>, and <strong>Rape</strong> across all 50 US states in 1973, along with <strong>UrbanPop</strong> (percent urban population).
                                <br>A data science student writes the following R pipeline:
                            </p>
                            <pre class="r-code">data("USArrests")
# Normalize data using scale()
scaled_arrests &lt;- scale(USArrests)

# Set random seed and run K-means
set.seed(123)
km_model &lt;- kmeans(scaled_arrests, centers = 4, nstart = 20)</pre>

                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>What is the exact theoretical value and range for the <strong>Total Sum of Squares (TSS)</strong> of this standardized dataset?</li>
                                <li>Report the individual <strong>Within-Cluster Sum of Squares (WSS)</strong> for each of the 4 clusters obtained by the model.</li>
                                <li>Report the <strong>size (number of states)</strong> assigned to each cluster.</li>
                                <li>Compute the <strong>Between-Cluster Sum of Squares (BCSS)</strong> and determine which range it falls into ($100\\text{–}200$, $200\\text{–}300$, or $300\\text{–}350$).</li>
                                <li>Calculate the percentage of total variance explained by this 4-cluster model ($\\text{BCSS} / \\text{TSS} \\times 100\\%$).</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Determine Total Sum of Squares (TSS)</div>
                                        <p>
                                            The dataset contains $n = 50$ states (rows) and $p = 4$ quantitative variables (columns).
                                            Because the data is normalized via <code class="inline-code">scale()</code>, each column has sample variance $s^2 = 1$.
                                            $$\\text{TSS} = \\sum_{j=1}^p \\sum_{i=1}^n (x_{ij} - \\bar{x}_j)^2 = \\sum_{j=1}^p (n - 1)s_j^2 = (50 - 1) \\times 4 = 49 \\times 4 = \\mathbf{196}$$
                                            Therefore, the Total Sum of Squares is exactly <strong>196</strong>, falling strictly in the range <strong>100 – 200</strong>!
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Individual Cluster Within-SS Values</div>
                                        <p>
                                            Extracting <code class="inline-code">km_model$withinss</code> in R (with <code class="inline-code">set.seed(123)</code>, <code class="inline-code">centers = 4</code>, <code class="inline-code">nstart = 20</code>):
                                            $$\\mathbf{\\{8.316061, \\; 11.952463, \\; 16.212213, \\; 19.922437\\}}$$
                                            Total within-cluster sum of squares:
                                            $$\\text{WSS} = 8.316061 + 11.952463 + 16.212213 + 19.922437 = \\mathbf{56.40317}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Cluster Sizes (State Allocations)</div>
                                        <p>
                                            Extracting <code class="inline-code">km_model$size</code>:
                                            $$\\mathbf{\\{8, \\; 13, \\; 16, \\; 13\\}}$$
                                            Notice that $8 + 13 + 16 + 13 = 50$ states (total accounted for).
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: Compute Between-Cluster Sum of Squares (BCSS)</div>
                                        <p>
                                            Applying the fundamental clustering identity:
                                            $$\\text{BCSS} = \\text{TSS} - \\text{WSS} = 196 - 56.40317 = \\mathbf{139.5968}$$
                                            Therefore, the BCSS value is $\\approx 139.60$, which falls squarely into the range <strong>100 – 200</strong>!
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 5: Percentage of Variance Explained</div>
                                        <p>
                                            $$\\frac{\\text{BCSS}}{\\text{TSS}} = \\frac{139.5968}{196} = 0.712228 \\implies \\mathbf{71.22\\%}$$
                                            The 4-cluster model captures over $71\\%$ of the total multi-attribute variation among US states.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 6: Complete R Verification Script</div>
                                        <pre class="r-code">data("USArrests")
scaled_arrests &lt;- scale(USArrests)

set.seed(123)
km &lt;- kmeans(scaled_arrests, centers = 4, nstart = 20)

cat("Cluster Sizes:", km$size, "\\n")               # 8 13 16 13
cat("Within-SS per cluster:", round(km$withinss, 6), "\\n")
# 8.316061 11.952463 16.212213 19.922437
cat("Total WSS:", round(km$tot.withinss, 4), "\\n") # 56.4032
cat("Between-SS:", round(km$betweenss, 4), "\\n")   # 139.5968 (Range 100-200)
cat("Total-SS:", km$totss, "\\n")                  # 196 (Range 100-200)
cat("Variance Explained:", round(km$betweenss / km$totss * 100, 2), "%\\n") # 71.22%</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Summary: Within-SS = [8.32, 11.95, 16.21, 19.92], Sizes = [8, 13, 16, 13], Total SS = 196 (100-200), BCSS = 139.6 (100-200).
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

print("Week 8 module loaded.")
