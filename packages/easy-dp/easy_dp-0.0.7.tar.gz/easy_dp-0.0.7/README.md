# easy-dp

This library provides a simple way to implement differential privacy in PyTorch. The focus is only on supporting multi-gpu training with FSDP to allow for large models.

Note: the code is heavily based on [private-transformers](https://github.com/lxuechen/private-transformers)

## Installation

    pip install easy-dp

## Usage

    from easy_dp import PrivacyEngine

    privacy_engine = PrivacyEngine(
        len_dataset=len(train_dataset),
        batch_size=batch_size,
        max_grad_norm=max_grad_norm,
        num_epochs=num_epochs,
        target_epsilon=target_epsilon,
        target_delta=target_delta,
    )

Compute the gradient of a single sample, then clip it:

    privacy_engine.clip_gradient(model.parameters())

You can accumulate the gradients into a variable, for example here we use the `summed_clipped_gradients` attribute. Then add noise to the accumulated gradients and divide by the batch size before saving the gradients to the model parameters:

    for param in model.parameters():
        param.grad = privacy_engine.add_noise(param.summed_clipped_gradients)
        param.grad = param.grad / batch_size

Now you can call `optimizer.step()` to update the model parameters.

## Upload to PyPI

    python -m build

    twine upload dist/*